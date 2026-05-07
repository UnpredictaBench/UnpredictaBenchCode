import argparse
import json
import os
import random
import re
import time
from typing import Any, Dict, List, Optional, Tuple
from openai import OpenAI
from tqdm import tqdm

# === Configure your API settings here ===
API_BASE_URL = "https://openrouter.ai/api/v1"
API_KEY = ""
API_PROVIDER = ""

NUMBER_PATTERN = r"[+-]?(?:\d+(?:\.\d+)?|\.\d+)(?:[eE][+-]?\d+)?"

RESUME_REQUIRED_FIELDS = (
    "model_outputs",
    "reasoning_texts",
    "extracted_numbers",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run prompts sequentially with reasoning models and extract numbers from reasoning"
    )
    parser.add_argument("--input_file", type=str, default="", help="Path to the input JSON file")
    parser.add_argument("--output_dir", type=str, default="outputs_reasoning", help="Directory to save the outputs")
    parser.add_argument("--model", type=str, default="", help="Model ID for generation")
    parser.add_argument(
        "--api_key",
        type=str,
        default=API_KEY,
        help="API key for the provider",
    )
    parser.add_argument(
        "--provider",
        type=str,
        default=API_PROVIDER,
        help="Single OpenRouter provider name (optional)",
    )
    parser.add_argument("--temp", type=float, default=1, help="Temperature for generation")
    parser.add_argument("--max_tokens", type=int, default=4096, help="Max tokens to generate")
    parser.add_argument("--max_retries", type=int, default=5, help="Max retry attempts for transient API errors")
    parser.add_argument("--retry_base_sleep", type=float, default=5.0, help="Base seconds for exponential backoff")
    parser.add_argument("--limit", type=int, default=None, help="Limit the number of prompts to process")
    parser.add_argument("--verbose", action="store_true", help="Print responses to console")
    parser.add_argument(
        "--resume",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Resume from existing per-prompt output files in output_dir (default: enabled)",
    )
    parser.add_argument(
        "--numbers_target",
        type=int,
        default=100,
        help="How many unique numbers to collect per task",
    )
    parser.add_argument(
        "--max_attempts",
        type=int,
        default=100,
        help="Maximum generation attempts per task",
    )
    parser.add_argument(
        "--dry_run",
        action="store_true",
        help="Process only the first 5 tasks",
    )
    return parser.parse_args()


def validate_args(args: argparse.Namespace) -> Tuple[bool, List[str]]:
    errors: List[str] = []

    if not args.model:
        errors.append("--model is required.")

    if not args.api_key:
        errors.append("--api_key is required.")

    if args.numbers_target < 1:
        errors.append("--numbers_target must be >= 1")

    if args.max_attempts < 1:
        errors.append("--max_attempts must be >= 1")

    if args.max_retries < 1:
        errors.append("--max_retries must be >= 1")

    return (len(errors) == 0), errors


def build_client(base_url: str, api_key: str) -> OpenAI:
    if not base_url:
        raise ValueError("API base URL is required")
    if not api_key:
        raise ValueError("API key is required")
    return OpenAI(base_url=base_url, api_key=api_key)


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


def extract_numbers_from_reasoning(
    task_prompt: str,
    model_reasoning: str,
) -> List[float]:
    if not model_reasoning:
        return []

    prompt_numbers = set(re.findall(NUMBER_PATTERN, task_prompt or ""))
    matches = re.findall(NUMBER_PATTERN, model_reasoning)

    numbers: List[float] = []
    for match in matches:
        if match in prompt_numbers:
            continue
        try:
            numbers.append(float(match))
        except ValueError:
            continue
        
    return numbers


def extract_numbers_from_output(output_text: str) -> List[float]:
    text = (output_text or "").strip()
    if not text:
        return []

    matches = re.findall(NUMBER_PATTERN, text)
    numbers: List[float] = []
    for match in matches:
        try:
            numbers.append(float(match))
        except ValueError:
            continue

    return numbers


def make_safe_id(prompt_id: Any) -> str:
    return str(prompt_id).replace("/", "_").replace(" ", "_").replace(":", "_")


def extract_reasoning_text(message: Any) -> str:
    reasoning = getattr(message, "reasoning", None)
    if isinstance(reasoning, str) and reasoning.strip():
        return reasoning.strip()

    model_extra = getattr(message, "model_extra", None)
    if isinstance(model_extra, dict):
        extra_reasoning = model_extra.get("reasoning")
        if isinstance(extra_reasoning, str) and extra_reasoning.strip():
            return extra_reasoning.strip()

    return ""


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


def load_existing_result_for_item(
    item: Dict[str, Any],
    output_dir: str,
    numbers_target: int,
) -> Optional[Dict[str, Any]]:
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

    for field in RESUME_REQUIRED_FIELDS:
        if field not in existing:
            print(f"Warning: existing result for prompt {prompt_id} is missing {field}; reprocessing.")
            return None

    extracted_numbers = existing.get("extracted_numbers")
    if isinstance(extracted_numbers, list) and len(extracted_numbers) >= numbers_target:
        return existing

    return None


def process_prompt_item(
    item: Dict[str, Any],
    client: OpenAI,
    args: argparse.Namespace,
) -> Optional[Dict[str, Any]]:
    prompt_text = item.get("prompt_text")
    prompt_id = item.get("id", "unknown_id")

    if not prompt_text:
        print(f"Skipping prompt {prompt_id}: missing 'prompt_text'.")
        return None

    collected_numbers: List[float] = []
    reasoning_texts: List[str] = []
    model_outputs: List[str] = []

    for attempt in range(1, args.max_attempts + 1):
        if len(collected_numbers) >= args.numbers_target:
            break

        generation_call_params = {
            "model": args.model,
            "messages": [{"role": "user", "content": prompt_text}],
            "temperature": args.temp,
            "max_tokens": args.max_tokens,
            "extra_body": {
                "reasoning": {
                    "max_tokens": 4000,
                }
            },
        }

        if args.provider:
            generation_call_params["extra_body"]["provider"] = {
                "order": [args.provider],
                "only": [args.provider],
                "allow_fallbacks": False,
            }

        response = create_chat_completion_with_retry(
            client=client,
            call_params=generation_call_params,
            max_retries=args.max_retries,
            retry_base_sleep=args.retry_base_sleep,
            context_label=f"generation for {prompt_id}",
        )

        message = response.choices[0].message
        model_output = getattr(message, "content", None) or ""
        reasoning_text = getattr(message, "reasoning", None) or ""
        if not isinstance(reasoning_text, str) or not reasoning_text.strip():
            reasoning_text = extract_reasoning_text(message)

        if args.verbose:
            print(
                f"\n--- ID: {prompt_id} (attempt {attempt}/{args.max_attempts}) ---\n"
                f"OUTPUT:\n{model_output}\n"
                f"REASONING:\n{reasoning_text}\n"
            )

        model_outputs.append(model_output)
        reasoning_texts.append(reasoning_text)

        reasoning_numbers = extract_numbers_from_reasoning(
            task_prompt=prompt_text,
            model_reasoning=reasoning_text,
        )

        output_numbers = extract_numbers_from_output(model_output)

        new_numbers = reasoning_numbers + output_numbers
        collected_numbers.extend(new_numbers)

        if len(collected_numbers) >= args.numbers_target:
            break

    result_item = item.copy()
    result_item["model_used"] = args.model
    result_item["temperature"] = args.temp
    result_item["max_tokens"] = args.max_tokens
    result_item["numbers_target"] = args.numbers_target
    result_item["generation_attempts_used"] = len(model_outputs)
    result_item["reasoning_texts"] = reasoning_texts
    result_item["model_outputs"] = model_outputs
    result_item["extracted_numbers"] = collected_numbers[: args.numbers_target]

    return result_item


def main() -> None:
    args = parse_args()
    is_valid, validation_errors = validate_args(args)
    if not is_valid:
        for err in validation_errors:
            print(f"Error: {err}")
        return

    try:
        data = load_input_data(args.input_file, args.limit)
        if args.dry_run:
            data = data[:5]
        output_dir = ensure_output_dir(args.output_dir)
        client = build_client(API_BASE_URL, args.api_key)
    except Exception as exc:
        print(f"Error during setup: {exc}")
        return

    print(
        f"Processing {len(data)} prompts sequentially with model {args.model} "
        f"(temp={args.temp}, numbers_target={args.numbers_target}, max_attempts={args.max_attempts}, resume={args.resume})..."
    )

    indexed_results: Dict[int, Dict[str, Any]] = {}
    pending_items: List[Tuple[int, Dict[str, Any]]] = []

    if args.resume:
        for idx, item in enumerate(data):
            existing_result = load_existing_result_for_item(item, output_dir, args.numbers_target)
            if existing_result is not None:
                indexed_results[idx] = existing_result
            else:
                pending_items.append((idx, item))
        print(f"Resume enabled: found {len(indexed_results)} existing results, {len(pending_items)} prompts pending.")
    else:
        pending_items = list(enumerate(data))
        print(f"Resume disabled: processing all {len(pending_items)} prompts.")

    for idx, item in tqdm(pending_items):
        prompt_id = item.get("id", "unknown_id")
        try:
            result_item = process_prompt_item(
                item=item,
                client=client,
                args=args,
            )
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
