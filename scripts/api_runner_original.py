import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
import os
import random
import re
import time
from typing import Any, Dict, List, Optional, Tuple
from openai import OpenAI
from tqdm import tqdm

EXTRACTION_SYSTEM_PROMPT = "You are a precise JSON extractor. Return only valid JSON."

EXTRACTION_PROMPT_TEMPLATE = """Analyze the model output below and decide whether it reports a number.
The model output is the response of another LLM that was asked to output a random number from a specific distribution; the distribution details do not matter here.

Model output:
{model_output}

Rules:
1. If the output does not report any number (only code, explanation, etc.), return {{"rationale": "No number found in the model output", "number": null}}
2. If the output reports a number, return {{"rationale": "The model mentioned <<the_number>> in the exact text <<exact_span>> at <<exact_location>> of the output", "number": <the_number>}}
3. There may exist some cases that the model output is incomplete, malformed, or does not follow instructions. In those cases, you may see some numbers unrelated to the final answer (like repeating the list of parameters from the input distribution); therefore, if you cannot confidently identify a number being reported as the final answer, default to {{"rationale": "Cannot confidently identify a number being reported as the final answer", "number": null}}.
4. Only use numbers that are explicitly present in the model output. Do not infer, calculate, or extract values from variable names, code structure, or explanatory text unless they are clearly presented as the answer.
5. For <<exact_span>>, copy the smallest exact substring from the model output that contains the reported number.
6. For <<exact_location>>, briefly describe where that exact span occurs in the output. Example templates include "beginning of the output", "middle of the output", "end of the output", "first line", and "last line", but any other concise, precise location description is allowed.
7. Do NOT quote any number unless it is the final reported answer.
8. Before finalizing, verify that the JSON is valid, the rationale matches the chosen number or null outcome, and any number returned is explicitly presented in the model output as the final answer.
9. Return only one valid JSON object with exactly these keys and no extra text, markdown, or formatting: {{"rationale": "No number found in the model output", "number": null}} or {{"rationale": "The model mentioned <<the_number>> in the exact text <<exact_span>> at <<exact_location>> of the output", "number": <the_number>}}.
"""
RESUME_REQUIRED_FIELDS = (
    "model_output",
    "finish_reason",
    "generation_attempts_used",
    "extract_number_enabled",
    "reinforced_prompt_used",
)

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run prompts from a JSON file using OpenRouter/vLLM with optional numeric extraction"
    )
    parser.add_argument("--input_file", type=str, default="", help="Path to the input JSON file")
    parser.add_argument("--output_dir", type=str, default="outputs", help="Directory to save the outputs")
    parser.add_argument(
        "--api_provider",
        type=str,
        choices=["openrouter", "vllm"],
        default="openrouter",
        help="API provider to use",
    )
    parser.add_argument(
        "--model",
        type=str,
        default="",
        help="Model ID (OpenRouter) or model name (vLLM)",
    )
    parser.add_argument("--api_key", type=str, help="API Key")
    parser.add_argument("--temp", type=float, default=0.7, help="Temperature for generation")
    parser.add_argument("--max_tokens", type=int, default=4096, help="Max tokens to generate")
    parser.add_argument(
        "--parallel_requests",
        type=int,
        default=128,
        help="Number of prompts to process concurrently",
    )
    # Retries transient API failures like rate limits, timeouts, and 5xx responses.
    parser.add_argument("--max_retries", type=int, default=5, help="Max retry attempts for transient API errors")
    parser.add_argument(
        "--retry_base_sleep",
        type=float,
        default=5.0,
        help="Base seconds for exponential backoff before jitter",
    )
    parser.add_argument("--limit", type=int, default=None, help="Limit the number of prompts to process")
    parser.add_argument("--verbose", action="store_true", help="Print responses to console")
    parser.add_argument(
        "--resume",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Resume from existing per-prompt output files in output_dir (default: enabled)",
    )
    parser.add_argument(
        "--openrouter_provider",
        type=str,
        default="",
        help="Comma-separated OpenRouter provider order (e.g., 'OpenAI,Anthropic')",
    )
    parser.add_argument(
        "--extract_number",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Enable/disable numeric extraction from each model output (default: enabled)",
    )
    # Retries the main generation when extraction finds no usable number.
    parser.add_argument(
        "--number_extraction_retries",
        type=int,
        default=5,
        help="How many generation attempts to make if extracted output has no number",
    )
    parser.add_argument(
        "--number_extractor_model",
        type=str,
        default="",
        help="Model used for extraction call (default: same as --model). Use 'regex' to extract numbers from {{number}} patterns instead of using an LLM",
    )
    parser.add_argument(
        "--number_extractor_api_provider",
        type=str,
        choices=["openrouter", "vllm"],
        default="",
        help="API provider for number extractor (default: same as --api_provider)",
    )
    parser.add_argument(
        "--number_extractor_api_key",
        type=str,
        default="",
        help="API key for number extractor provider (default: same as --api_key)",
    )
    parser.add_argument(
        "--number_extraction_temp",
        type=float,
        default=0.3,
        help="Temperature for number extraction call",
    )
    parser.add_argument(
        "--number_extraction_max_tokens",
        type=int,
        default=128,
        help="Max tokens for number extraction call",
    )
    return parser.parse_args()


def validate_args(args: argparse.Namespace) -> Tuple[bool, List[str]]:
    errors: List[str] = []

    if args.api_provider == "openrouter" and not args.openrouter_provider:
        errors.append("--openrouter_provider is required when --api_provider openrouter is selected.")

    if not args.api_key:
        errors.append("API key must be provided via --api_key.")

    if args.number_extraction_retries < 1:
        errors.append("--number_extraction_retries must be >= 1")

    if args.max_retries < 1:
        errors.append("--max_retries must be >= 1")

    if args.parallel_requests < 1:
        errors.append("--parallel_requests must be >= 1")

    return (len(errors) == 0), errors


def build_client(api_provider: str, api_key: str) -> OpenAI:
    if api_provider == "openrouter":
        return OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)
    if api_provider == "vllm":
        return OpenAI(base_url="http://localhost:8000/v1", api_key=api_key)
    raise ValueError(f"Unsupported API provider: {api_provider}")


def load_input_data(input_file: str, limit: Optional[int]) -> List[Dict[str, Any]]:
    input_path = os.path.abspath(input_file)
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")

    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if limit:
        data = data[:limit]
    return data


def ensure_output_dir(output_dir: str) -> str:
    out_dir = os.path.abspath(output_dir)
    os.makedirs(out_dir, exist_ok=True)
    return out_dir


def parse_provider_order(args: argparse.Namespace) -> List[str]:
    if args.api_provider != "openrouter" or not args.openrouter_provider:
        return []

    provider_order = [p.strip() for p in args.openrouter_provider.split(",") if p.strip()]
    if not provider_order:
        raise ValueError("--openrouter_provider parsed to an empty list. Provide at least one provider.")
    return provider_order


def is_retryable_error(msg: str) -> bool:
    msg_lower = msg.lower()
    return (
        "429" in msg_lower
        or "resource_exhausted" in msg_lower
        or "rate" in msg_lower
        or "quota" in msg_lower
        or "retry" in msg_lower
        or "timeout" in msg_lower
        or "timed out" in msg_lower
        or "temporarily" in msg_lower
        or "connection reset" in msg_lower
        or "connection aborted" in msg_lower
        or "retry later" in msg_lower
        or "please try again" in msg_lower
        or "502" in msg_lower
        or "503" in msg_lower
        or "504" in msg_lower
        or "server error" in msg_lower
    )


def parse_retry_after_seconds(exc: Exception) -> Optional[float]:
    retry_after: Optional[float] = None

    headers = getattr(exc, "response", None)
    if headers and hasattr(headers, "headers"):
        ra_val = headers.headers.get("Retry-After")
        if ra_val:
            try:
                retry_after = float(ra_val)
            except ValueError:
                pass

    msg = str(exc)
    patterns = [
        r"retry\s+in\s+(\d+(?:\.\d+)?)s",
        r"retrydelay['\"]?[:=]\s*['\"]?(\d+(?:\.\d+)?)(?:s|sec|seconds)?",
        r"retry[- ]after[: ](\d+(?:\.\d+)?)",
    ]

    for pattern in patterns:
        match = re.search(pattern, msg, flags=re.IGNORECASE)
        if match:
            try:
                retry_after = float(match.group(1))
                break
            except ValueError:
                continue

    return retry_after


def build_call_params(
    api_provider: str,
    model: str,
    messages: List[Dict[str, str]],
    temperature: float,
    max_tokens: int,
    provider_order: Optional[List[str]] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }

    if api_provider == "openrouter":
        extra_body: Dict[str, Any] = {}
        if provider_order:
            extra_body["provider"] = {
                "order": provider_order,
                "allow_fallbacks": False,
                "only": provider_order,
            }
        extra_body["reasoning"] = {"effort": "none"}
        if extra_body:
            params["extra_body"] = extra_body

    return params


def create_chat_completion_with_retry(
    client: OpenAI,
    call_params: Dict[str, Any],
    max_retries: int,
    retry_base_sleep: float,
    context_label: str,
) -> Any:
    retries = max(1, max_retries)

    for attempt in range(retries):
        try:
            return client.chat.completions.create(**call_params)
        except Exception as exc:
            msg = str(exc)
            retryable = is_retryable_error(msg)
            if retryable and attempt < retries - 1:
                hinted = parse_retry_after_seconds(exc)
                if hinted is not None:
                    wait_s = min(300.0, max(0.5, hinted))
                else:
                    base = max(0.5, retry_base_sleep)
                    wait_s = min(120.0, base * (2 ** attempt))

                wait_s += random.uniform(0, 1)
                print(
                    f"Transient error during {context_label}; retrying in {wait_s:.1f}s "
                    f"(attempt {attempt + 1}/{retries}). Error: {msg}"
                )
                time.sleep(wait_s)
                continue
            raise

    raise RuntimeError(f"Failed after retries for {context_label}")


def extract_number_with_regex(model_output: str) -> Dict[str, Any]:
    """Extract a number from model output using regex, preferring bracketed format."""
    text = (model_output or "").strip()

    # Prefer bracketed number pattern anywhere in the output.
    braced_pattern = r"\{\s*([+-]?(?:\d+(?:\.\d+)?|\.\d+)(?:[eE][+-]?\d+)?)\s*\}"
    braced_match = re.search(braced_pattern, text)
    if braced_match:
        number_str = braced_match.group(1)
        try:
            number_value = float(number_str)
            exact_span = braced_match.group(0)
            return {
                "rationale": f"Regex extracted number {number_value} from pattern {exact_span}",
                "number": number_value,
            }
        except ValueError:
            return {"rationale": "Could not convert matched number to float", "number": None}

    # Fallback: accept outputs that are only a plain number.
    plain_output_pattern = r"^\s*([+-]?(?:\d+(?:\.\d+)?|\.\d+)(?:[eE][+-]?\d+)?)\s*$"
    plain_match = re.match(plain_output_pattern, text)
    if plain_match:
        number_str = plain_match.group(1)
        try:
            number_value = float(number_str)
            return {
                "rationale": f"Regex extracted number {number_value} from plain numeric output",
                "number": number_value,
            }
        except ValueError:
            return {"rationale": "Could not convert matched number to float", "number": None}

    return {
        "rationale": "No number found via regex (expected a plain number output or a {number} pattern)",
        "number": None,
    }


def parse_extractor_json(result_text: str) -> Optional[Dict[str, Any]]:
    text = result_text.strip()

    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text, flags=re.IGNORECASE)
        text = re.sub(r"\s*```$", "", text)

    start = text.find("{")
    end = text.rfind("}")
    if start != -1 and end != -1 and end >= start:
        text = text[start : end + 1]

    try:
        parsed = json.loads(text)
    except Exception:
        return None

    if not isinstance(parsed, dict):
        return None

    if "rationale" not in parsed or "number" not in parsed:
        return None

    rationale = (parsed.get("rationale"))
    number_value = parsed.get("number")

    if number_value is not None:
        try:
            number_value = float(number_value)
        except (ValueError, TypeError):
            return {"rationale": "None", "number": None}

    if not rationale:
        number_value = None

    return {"rationale": rationale, "number": number_value}


def extract_number_with_provider(
    model_output: str,
    client: OpenAI,
    api_provider: str,
    extractor_model: str,
    extractor_api_provider: str,
    extractor_api_key: str,
    max_retries: int,
    retry_base_sleep: float,
    extraction_temperature: float,
    extraction_max_tokens: int,
) -> Dict[str, Any]:
    # Use regex extraction if extractor_model is "regex"
    if extractor_model.lower() == "regex":
        return extract_number_with_regex(model_output)
    
    prompt = EXTRACTION_PROMPT_TEMPLATE.format(model_output=model_output)
    extractor_client = client
    extractor_provider = extractor_api_provider
    
    if extractor_api_provider and extractor_api_provider != api_provider:
        extractor_client = build_client(extractor_api_provider, extractor_api_key)
        extractor_provider = extractor_api_provider
    else:
        extractor_provider = api_provider


    call_params = build_call_params(
        api_provider=extractor_provider,
        model=extractor_model,
        messages=[
            {"role": "system", "content": EXTRACTION_SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        temperature=extraction_temperature,
        max_tokens=extraction_max_tokens,
    )

    try:
        response = create_chat_completion_with_retry(
            client=extractor_client,
            call_params=call_params,
            max_retries=max_retries,
            retry_base_sleep=retry_base_sleep,
            context_label=f"number extraction ({extractor_model})",
        )
        result_text = (response.choices[0].message.content or "").strip()
        parsed = parse_extractor_json(result_text)
        if parsed is None:
            return {"rationale": "None", "number": None}
        return parsed
    except Exception as exc:
        print(f"Error during number extraction: {exc}")
        return {"rationale": "None", "number": None}


def make_safe_id(prompt_id: Any) -> str:
    return str(prompt_id).replace("/", "_").replace(" ", "_").replace(":", "_")


def build_followup_number_only_prompt(
    original_prompt: str,
    failed_attempts: int,
    last_output: str,
) -> str:
    previous_output = (last_output or "").strip()

    followup_instruction = (
        f"\n\nIMPORTANT: I have already asked you {failed_attempts} times, and your previous output was:\n"
        f"\"\"\"\n{previous_output}\n\"\"\"\"\n"
        "That output did not contain any extractable final number. "
        "Do not explain, do not provide code, and do not add any extra text. "
        "Return only the final sampled random number as instructed."
    )

    return original_prompt + followup_instruction


def process_prompt_item(
    item: Dict[str, Any],
    args: argparse.Namespace,
    provider_order: List[str],
) -> Optional[Dict[str, Any]]:
    prompt_text = item.get("prompt_text")
    prompt_id = item.get("id", "unknown_id")

    if not prompt_text:
        print(f"Skipping prompt {prompt_id}: missing 'prompt_text'.")
        return None

    extractor_model = args.number_extractor_model.strip() or args.model
    extractor_api_provider = args.number_extractor_api_provider.strip() or args.api_provider
    extractor_api_key = args.number_extractor_api_key.strip() or args.api_key
    generation_attempts = args.number_extraction_retries if args.extract_number else 1

    selected_output_text: Optional[str] = None
    selected_finish_reason: Optional[str] = None
    extraction_result: Dict[str, Any] = {"rationale": "None", "number": None}
    used_generation_attempts = 0
    reinforced_prompt_used = False
    client = build_client(args.api_provider, args.api_key)

    followup_attempts = 1 if args.extract_number else 0
    total_generation_attempts = generation_attempts + followup_attempts

    for gen_attempt in range(1, total_generation_attempts + 1):
        used_generation_attempts = gen_attempt

        current_prompt_text = prompt_text
        is_followup_attempt = gen_attempt > generation_attempts
        if is_followup_attempt:
            reinforced_prompt_used = True
            current_prompt_text = build_followup_number_only_prompt(
                original_prompt=prompt_text,
                failed_attempts=generation_attempts,
                last_output=selected_output_text or "",
            )

        generation_call_params = build_call_params(
            api_provider=args.api_provider,
            model=args.model,
            messages=[{"role": "user", "content": current_prompt_text}],
            temperature=args.temp,
            max_tokens=args.max_tokens,
            provider_order=provider_order,
        )

        response = create_chat_completion_with_retry(
            client=client,
            call_params=generation_call_params,
            max_retries=args.max_retries,
            retry_base_sleep=args.retry_base_sleep,
            context_label=f"generation for {prompt_id}",
        )

        model_output = response.choices[0].message.content
        finish_reason = getattr(response.choices[0], "finish_reason", None)

        if args.verbose:
            print(f"\n--- ID: {prompt_id} (attempt {gen_attempt}/{generation_attempts}) ---\n{model_output}\n")

        selected_output_text = model_output
        selected_finish_reason = finish_reason

        if not args.extract_number:
            break

        extraction_result = extract_number_with_provider(
            model_output=model_output,
            client=client,
            api_provider=args.api_provider,
            extractor_model=extractor_model,
            extractor_api_provider=extractor_api_provider,
            extractor_api_key=extractor_api_key,
            max_retries=args.max_retries,
            retry_base_sleep=args.retry_base_sleep,
            extraction_temperature=args.number_extraction_temp,
            extraction_max_tokens=args.number_extraction_max_tokens,
        )

        if extraction_result.get("number") is not None:
            break

        if gen_attempt < generation_attempts:
            print(
                f"No number extracted for prompt {prompt_id} on attempt {gen_attempt}/{generation_attempts}; retrying generation."
            )
        elif gen_attempt == generation_attempts and followup_attempts > 0:
            print(
                f"No number extracted for prompt {prompt_id} after {generation_attempts} attempts; "
                "retrying once with reinforced number-only instructions."
            )

    result_item = item.copy()
    result_item["model_output"] = selected_output_text
    result_item["model_used"] = args.model
    result_item["api_provider"] = args.api_provider
    result_item["temperature"] = args.temp
    result_item["max_tokens"] = args.max_tokens
    result_item["finish_reason"] = selected_finish_reason
    result_item["generation_attempts_used"] = used_generation_attempts
    result_item["extract_number_enabled"] = bool(args.extract_number)
    result_item["reinforced_prompt_used"] = reinforced_prompt_used
    result_item["number_extractor_model"] = extractor_model if args.extract_number else None
    result_item["rationale"] = extraction_result.get("rationale") if args.extract_number else None
    result_item["extracted_number"] = extraction_result.get("number") if args.extract_number else None

    if args.api_provider == "openrouter":
        result_item["openrouter_provider_order"] = provider_order if provider_order else None
        result_item["openrouter_allow_fallbacks"] = False if provider_order else None
    else:
        result_item["openrouter_provider_order"] = None

    return result_item


def save_individual_result(result_item: Dict[str, Any], output_dir: str) -> str:
    prompt_id = result_item.get("id", "unknown_id")
    safe_id = make_safe_id(prompt_id)
    output_file = os.path.join(output_dir, f"{safe_id}.json")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(result_item, f, indent=2)
    return output_file


def save_summary(results: List[Dict[str, Any]], output_dir: str) -> str:
    final_output = os.path.join(output_dir, "all_results.json")
    with open(final_output, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    return final_output


def load_existing_result_for_item(item: Dict[str, Any], output_dir: str) -> Optional[Dict[str, Any]]:
    prompt_id = item.get("id", "unknown_id")
    safe_id = make_safe_id(prompt_id)
    output_file = os.path.join(output_dir, f"{safe_id}.json")

    if not os.path.exists(output_file):
        return None

    try:
        with open(output_file, "r", encoding="utf-8") as f:
            existing = json.load(f)
    except Exception as exc:
        print(f"Warning: could not parse existing result for prompt {prompt_id} ({output_file}): {exc}")
        return None

    if not isinstance(existing, dict):
        print(f"Warning: existing result for prompt {prompt_id} is not a JSON object; reprocessing.")
        return None

    if item.get("id") is not None and existing.get("id") != item.get("id"):
        print(f"Warning: existing result id mismatch for prompt {prompt_id}; reprocessing.")
        return None

    for field in RESUME_REQUIRED_FIELDS:
        if field not in existing:
            print(f"Warning: existing result for prompt {prompt_id} is missing {field}; reprocessing.")
            return None

    if existing.get("extract_number_enabled"):
        if "rationale" not in existing or "extracted_number" not in existing:
            print(
                f"Warning: existing extracted result for prompt {prompt_id} is incomplete; reprocessing."
            )
            return None

    return existing


def main() -> None:
    args = parse_args()
    is_valid, validation_errors = validate_args(args)
    if not is_valid:
        for err in validation_errors:
            print(f"Error: {err}")
        return

    try:
        provider_order = parse_provider_order(args)
        data = load_input_data(args.input_file, args.limit)
        output_dir = ensure_output_dir(args.output_dir)
    except Exception as exc:
        print(f"Error during setup: {exc}")
        return

    print(
        f"Processing {len(data)} prompts using {args.api_provider} with model {args.model} "
        f"(temp={args.temp}, extract_number={args.extract_number}, parallel_requests={args.parallel_requests}, "
        f"resume={args.resume})..."
    )

    indexed_results: Dict[int, Dict[str, Any]] = {}
    pending_items: List[Tuple[int, Dict[str, Any]]] = []

    if args.resume:
        for idx, item in enumerate(data):
            existing_result = load_existing_result_for_item(item, output_dir)
            if existing_result is not None:
                indexed_results[idx] = existing_result
            else:
                pending_items.append((idx, item))
        print(f"Resume enabled: found {len(indexed_results)} existing results, {len(pending_items)} prompts pending.")
    else:
        pending_items = list(enumerate(data))
        print(f"Resume disabled: processing all {len(pending_items)} prompts.")

    if args.parallel_requests == 1:
        for idx, item in tqdm(pending_items):
            prompt_id = item.get("id", "unknown_id")
            try:
                result_item = process_prompt_item(
                    item=item,
                    args=args,
                    provider_order=provider_order,
                )
                if result_item is None:
                    continue

                indexed_results[idx] = result_item
                save_individual_result(result_item, output_dir)
            except Exception as exc:
                print(f"Error processing prompt {prompt_id}: {exc}")
    else:
        with ThreadPoolExecutor(max_workers=args.parallel_requests) as executor:
            future_to_index = {
                executor.submit(process_prompt_item, item, args, provider_order): idx
                for idx, item in pending_items
            }

            for future in tqdm(as_completed(future_to_index), total=len(future_to_index)):
                idx = future_to_index[future]
                prompt_id = data[idx].get("id", "unknown_id")
                try:
                    result_item = future.result()
                    if result_item is None:
                        continue

                    indexed_results[idx] = result_item
                    save_individual_result(result_item, output_dir)
                except Exception as exc:
                    print(f"Error processing prompt {prompt_id}: {exc}")

    results: List[Dict[str, Any]] = [indexed_results[i] for i in sorted(indexed_results)]

    final_output = save_summary(results, output_dir)

    print(f"\nDone! Processed {len(results)} prompts.")
    print(f"Results saved to: {output_dir}")
    print(f"Summary file: {final_output}")


if __name__ == "__main__":
    main()