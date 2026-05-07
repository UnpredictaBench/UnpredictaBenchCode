import argparse
import ast
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
import os
import re
import random
import time
from typing import Any, Dict, List, Optional, Tuple
from openai import OpenAI
from tqdm import tqdm

from runner_common import (
    build_call_params,
    build_client,
    create_chat_completion_with_retry,
    ensure_output_dir,
    ensure_boolean_optional_action,
    load_input_data,
    make_safe_id,
    parse_provider_order,
    parse_retry_after_seconds,
    save_summary,
    is_retryable_error,
    strip_json_fence,
)

ensure_boolean_optional_action(argparse)

EXTRACTION_PROFILE_NUMBER = "number"
EXTRACTION_PROFILE_SHUFFLING_LIST = "shuffling_list"
EXTRACTION_PROFILE_CHOICES = (
    EXTRACTION_PROFILE_NUMBER,
    EXTRACTION_PROFILE_SHUFFLING_LIST,
)

QWEN_NO_THINK_MODEL = "qwen/qwen3-32b"
QWEN_NO_THINK_PREFIX = "/no_think "

# Models that should receive an example-output suffix appended to the prompt
SUFFIX_MODELS = {
    "mistralai/Ministral-3-3B-Base-2512",
    "meta-llama/Llama-3.2-1B",
    "Qwen/Qwen3.5-2B-Base",
}
SUFFIX_TEXT = "\n\nA valid example for this question is:"

EXTRACTION_SYSTEM_PROMPT = "You are a precise JSON extractor. Return only valid JSON."

NUMBER_EXTRACTION_PROMPT_TEMPLATE = """Analyze the model output below and decide whether it reports a number.
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

NUMBER_EXTRACTION_PROMPT_TEMPLATE_MULTI = """Analyze the model output below and decide whether it reports exactly {expected_count} numeric values (the model was asked for multiple independent samples; distribution details do not matter here).

Model output:
{model_output}

Rules:
1. If the output does not clearly present exactly {expected_count} distinct final numeric answers, return {{"rationale": <string explaining why>, "numbers": null}}.
2. If the output clearly presents exactly {expected_count} final numeric answers (for example one number per line), return {{"rationale": <string summarizing where each value appears>, "numbers": [<n1>, <n2>, ...]}} with the numbers in the same order as in the model output (list length must be exactly {expected_count}).
3. Ignore numbers that are clearly not part of the final answers (parameters from the prompt, line numbers, unrelated code). If you cannot confidently identify exactly {expected_count} values as the final answers, return "numbers": null.
4. Only use numbers explicitly present in the model output. Do not infer or calculate unstated values.
5. Each element of "numbers" must be a JSON number (integer or float), not a string.
6. Return only one valid JSON object with exactly these keys and no extra text, markdown, or code fences: "rationale" (string) and "numbers" (JSON array of length {expected_count} or null).
"""

SHUFFLING_LIST_EXTRACTION_PROMPT_TEMPLATE = """Analyze the model output below and extract exactly one shuffled list answer.
The model output is the response of another LLM that was asked to return one possible shuffled list.

Model output:
{model_output}

Rules:
1. Return exactly one valid JSON object with exactly these keys: {"rationale": <string>, "value": <list_or_null>}.
2. If there is no valid list answer, return {"rationale": "No valid list found in the model output", "value": null}.
3. If multiple possible answers appear (for example text containing "or"), choose the first complete list that appears in the output.
4. The "value" field must be a JSON array (not a string) and must preserve the original order and element types.
5. Allowed list element types: string, integer, float.
6. If the model uses Python-style single quotes, convert them to equivalent JSON string values in "value".
7. Do not infer missing elements and do not synthesize a list.
8. Return only the JSON object and no additional text, markdown, or code fences.
"""

RESUME_REQUIRED_FIELDS = (
    "model_output",
    "finish_reason",
    "generation_attempts_used",
    "reinforced_prompt_used",
)

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run prompts from a JSON file using OpenRouter/vLLM with optional profile-based extraction"
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
        "--extract_value",
        dest="extract_value",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Enable/disable profile-based extraction from each model output (default: enabled)",
    )
    parser.add_argument(
        "--extract_number",
        dest="extract_value",
        action=argparse.BooleanOptionalAction,
        default=argparse.SUPPRESS,
        help=argparse.SUPPRESS,
    )
    # Retries the main generation when extraction finds no usable value.
    parser.add_argument(
        "--extraction_retries",
        dest="extraction_retries",
        type=int,
        default=5,
        help="How many generation attempts to make if extracted output has no usable value",
    )
    parser.add_argument(
        "--number_extraction_retries",
        dest="extraction_retries",
        type=int,
        default=argparse.SUPPRESS,
        help=argparse.SUPPRESS,
    )
    parser.add_argument(
        "--value_extractor_model",
        dest="value_extractor_model",
        type=str,
        default="",
        help=(
            "Model used for extraction call (default: same as --model). "
            "Use 'regex' to run profile-specific regex/json extraction instead of using an LLM"
        ),
    )
    parser.add_argument(
        "--number_extractor_model",
        dest="value_extractor_model",
        type=str,
        default=argparse.SUPPRESS,
        help=argparse.SUPPRESS,
    )
    parser.add_argument(
        "--extraction_profile",
        type=str,
        choices=list(EXTRACTION_PROFILE_CHOICES),
        default=EXTRACTION_PROFILE_NUMBER,
        help="Extraction schema/profile to use",
    )
    parser.add_argument(
        "--value_extractor_api_provider",
        dest="value_extractor_api_provider",
        type=str,
        choices=["openrouter", "vllm"],
        default="",
        help="API provider for value extractor (default: same as --api_provider)",
    )
    parser.add_argument(
        "--number_extractor_api_provider",
        dest="value_extractor_api_provider",
        type=str,
        choices=["openrouter", "vllm"],
        default=argparse.SUPPRESS,
        help=argparse.SUPPRESS,
    )
    parser.add_argument(
        "--value_extractor_api_key",
        dest="value_extractor_api_key",
        type=str,
        default="",
        help="API key for value extractor provider (default: same as --api_key)",
    )
    parser.add_argument(
        "--number_extractor_api_key",
        dest="value_extractor_api_key",
        type=str,
        default=argparse.SUPPRESS,
        help=argparse.SUPPRESS,
    )
    parser.add_argument(
        "--value_extraction_temp",
        dest="value_extraction_temp",
        type=float,
        default=0.3,
        help="Temperature for extraction call",
    )
    parser.add_argument(
        "--number_extraction_temp",
        dest="value_extraction_temp",
        type=float,
        default=argparse.SUPPRESS,
        help=argparse.SUPPRESS,
    )
    parser.add_argument(
        "--value_extraction_max_tokens",
        dest="value_extraction_max_tokens",
        type=int,
        default=128,
        help="Max tokens for extraction call",
    )
    parser.add_argument(
        "--number_extraction_max_tokens",
        dest="value_extraction_max_tokens",
        type=int,
        default=argparse.SUPPRESS,
        help=argparse.SUPPRESS,
    )
    parser.add_argument(
        "--prompt_find",
        type=str,
        default="",
        help="If non-empty, replace every occurrence of this substring in each prompt before calling the model",
    )
    parser.add_argument(
        "--prompt_replace",
        type=str,
        default="",
        help="Replacement for --prompt_find (may be empty to delete matches)",
    )
    parser.add_argument(
        "--output_dir_suffix",
        type=str,
        default="",
        help=(
            "Required when --prompt_find is non-empty. Short label for the output path segment "
            "temp_<temperature>_<suffix> (shell wrappers append it to --output_dir)."
        ),
    )
    parser.add_argument(
        "--expected_number_outputs",
        type=int,
        default=1,
        help=(
            "For extraction_profile=number: how many numeric answers the model output should contain "
            "(1 = single scalar in JSON 'number'; >1 = JSON 'numbers' array for LLM extractor and "
            "line-based parsing for regex)."
        ),
    )
    return parser.parse_args()


def validate_args(args: argparse.Namespace) -> Tuple[bool, List[str]]:
    errors: List[str] = []

    if args.api_provider == "openrouter" and not args.openrouter_provider:
        errors.append("--openrouter_provider is required when --api_provider openrouter is selected.")

    if not args.api_key:
        errors.append("API key must be provided via --api_key.")

    if args.extraction_retries < 1:
        errors.append("--extraction_retries must be >= 1")

    if args.max_retries < 1:
        errors.append("--max_retries must be >= 1")

    if args.parallel_requests < 1:
        errors.append("--parallel_requests must be >= 1")

    if args.prompt_find.strip():
        if not args.output_dir_suffix.strip():
            errors.append(
                "--output_dir_suffix is required when --prompt_find is set (non-empty after strip)."
            )
        elif "/" in args.output_dir_suffix or "\0" in args.output_dir_suffix:
            errors.append("--output_dir_suffix must not contain '/' or null bytes.")

    if args.expected_number_outputs < 1:
        errors.append("--expected_number_outputs must be >= 1")

    return (len(errors) == 0), errors


def normalize_list_value(value: Any) -> Optional[List[Any]]:
    if isinstance(value, tuple):
        value = list(value)

    if not isinstance(value, list):
        return None

    normalized: List[Any] = []
    for elem in value:
        if isinstance(elem, bool) or elem is None:
            return None
        if isinstance(elem, (int, float, str)):
            normalized.append(elem)
            continue
        return None

    return normalized


def parse_list_candidate(candidate_text: Any) -> Optional[List[Any]]:
    if isinstance(candidate_text, (list, tuple)):
        return normalize_list_value(candidate_text)

    if not isinstance(candidate_text, str):
        return None

    text = candidate_text.strip()
    if not text:
        return None

    if text.startswith("```"):
        text = re.sub(r"^```(?:json|python)?\s*", "", text, flags=re.IGNORECASE)
        text = re.sub(r"\s*```$", "", text)

    if not (text.startswith("[") and text.endswith("]")):
        match = re.search(r"\[[^\[\]]*\]", text, flags=re.DOTALL)
        if match:
            text = match.group(0)

    for parser in (json.loads, ast.literal_eval):
        try:
            parsed = parser(text)
        except Exception:
            continue

        normalized = normalize_list_value(parsed)
        if normalized is not None:
            return normalized

    return None


def parse_extractor_json(
    result_text: str,
    extraction_profile: str,
    expected_number_outputs: int = 1,
) -> Optional[Dict[str, Any]]:
    text = strip_json_fence(result_text)

    try:
        parsed = json.loads(text)
    except Exception:
        return None

    if not isinstance(parsed, dict):
        return None

    rationale = parsed.get("rationale")
    if not rationale:
        return None

    if extraction_profile == EXTRACTION_PROFILE_NUMBER:
        if expected_number_outputs <= 1:
            if "number" not in parsed:
                return None

            number_value = parsed.get("number")
            if number_value is not None:
                try:
                    number_value = float(number_value)
                except (ValueError, TypeError):
                    number_value = None

            return {
                "rationale": rationale,
                "number": number_value,
                "value": number_value,
            }

        raw_list = parsed.get("numbers")
        if raw_list is None and isinstance(parsed.get("number"), list):
            raw_list = parsed.get("number")
        if not isinstance(raw_list, list) or len(raw_list) != expected_number_outputs:
            return None

        numbers: List[float] = []
        for elem in raw_list:
            try:
                numbers.append(float(elem))
            except (ValueError, TypeError):
                return None

        return {
            "rationale": rationale,
            "number": None,
            "value": numbers,
        }

    if extraction_profile == EXTRACTION_PROFILE_SHUFFLING_LIST:
        value_candidate = parsed.get("value")
        if value_candidate is None:
            for alt_key in ("list", "answer", "shuffled_list"):
                if alt_key in parsed:
                    value_candidate = parsed.get(alt_key)
                    break

        parsed_list: Optional[List[Any]] = None
        if value_candidate is not None:
            parsed_list = parse_list_candidate(value_candidate)

        return {
            "rationale": rationale,
            "number": None,
            "value": parsed_list,
        }

    return None


def truncate_for_rationale(text: str, limit: int = 140) -> str:
    if len(text) <= limit:
        return text
    return text[: limit - 3] + "..."


def _extract_single_number_with_regex(text: str) -> Dict[str, Any]:
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
                "value": number_value,
            }
        except ValueError:
            return {"rationale": "Could not convert matched number to float", "number": None, "value": None}

    bracket_pattern = r"\[\s*([+-]?(?:\d+(?:\.\d+)?|\.\d+)(?:[eE][+-]?\d+)?)\s*\]"
    bracket_match = re.search(bracket_pattern, text)
    if bracket_match:
        number_str = bracket_match.group(1)
        try:
            number_value = float(number_str)
            exact_span = bracket_match.group(0)
            return {
                "rationale": f"Regex extracted number {number_value} from pattern {exact_span}",
                "number": number_value,
                "value": number_value,
            }
        except ValueError:
            return {"rationale": "Could not convert matched number to float", "number": None, "value": None}

    plain_output_pattern = r"^\s*([+-]?(?:\d+(?:\.\d+)?|\.\d+)(?:[eE][+-]?\d+)?)\s*$"
    plain_match = re.match(plain_output_pattern, text)
    if plain_match:
        number_str = plain_match.group(1)
        try:
            number_value = float(number_str)
            return {
                "rationale": f"Regex extracted number {number_value} from plain numeric output",
                "number": number_value,
                "value": number_value,
            }
        except ValueError:
            return {"rationale": "Could not convert matched number to float", "number": None, "value": None}

    return {
        "rationale": "No number found via regex (expected a plain number output or a {number}/[number] pattern)",
        "number": None,
        "value": None,
    }


def extract_number_with_regex(model_output: str, expected_count: int = 1) -> Dict[str, Any]:
    text = (model_output or "").strip()
    if expected_count <= 1:
        return _extract_single_number_with_regex(text)

    line_num_pattern = re.compile(r"^([+-]?(?:\d+(?:\.\d+)?|\.\d+)(?:[eE][+-]?\d+)?)$")
    lines = text.splitlines()
    numbers: List[float] = []
    line_idx = 0
    while line_idx < len(lines) and len(numbers) < expected_count:
        stripped = lines[line_idx].strip()
        line_idx += 1
        if not stripped:
            continue
        match = line_num_pattern.match(stripped)
        if not match:
            continue
        numbers.append(float(match.group(1)))

    if len(numbers) < expected_count:
        return {
            "rationale": (
                f"Regex found {len(numbers)} numeric line(s) after skipping non-numeric lines "
                f"but needed at least {expected_count}"
            ),
            "number": None,
            "value": None,
        }

    extra_numeric_lines = 0
    while line_idx < len(lines):
        stripped = lines[line_idx].strip()
        line_idx += 1
        if not stripped:
            continue
        if line_num_pattern.match(stripped):
            extra_numeric_lines += 1

    rationale = (
        f"Regex extracted the first {expected_count} numbers from line-oriented output "
        "(non-numeric lines skipped)"
    )
    if extra_numeric_lines > 0:
        rationale += f"; ignored {extra_numeric_lines} further numeric line(s) after that"

    return {
        "rationale": rationale,
        "number": None,
        "value": numbers,
    }


def extract_shuffling_list_with_regex(model_output: str) -> Dict[str, Any]:
    text = (model_output or "").strip()
    list_pattern = re.compile(r"\[[^\[\]]*\]", flags=re.DOTALL)

    for match in list_pattern.finditer(text):
        candidate = match.group(0)
        parsed_list = parse_list_candidate(candidate)
        if parsed_list is not None:
            return {
                "rationale": (
                    "Regex extracted the first valid list from exact span "
                    f"{truncate_for_rationale(candidate)}"
                ),
                "number": None,
                "value": parsed_list,
            }

    parsed_list = parse_list_candidate(text)
    if parsed_list is not None:
        return {
            "rationale": "Regex parsed the full output as a valid list",
            "number": None,
            "value": parsed_list,
        }

    return {
        "rationale": "No valid list found via regex/json parsing",
        "number": None,
        "value": None,
    }


def extract_with_regex(
    model_output: str,
    extraction_profile: str,
    expected_number_outputs: int = 1,
) -> Dict[str, Any]:
    if extraction_profile == EXTRACTION_PROFILE_NUMBER:
        return extract_number_with_regex(model_output, expected_number_outputs)
    if extraction_profile == EXTRACTION_PROFILE_SHUFFLING_LIST:
        return extract_shuffling_list_with_regex(model_output)
    return {"rationale": "Unsupported extraction profile", "number": None, "value": None}


def build_extraction_prompt(
    extraction_profile: str,
    model_output: str,
    expected_number_outputs: int = 1,
) -> str:
    if extraction_profile == EXTRACTION_PROFILE_NUMBER:
        if expected_number_outputs <= 1:
            return NUMBER_EXTRACTION_PROMPT_TEMPLATE.format(model_output=model_output)
        return NUMBER_EXTRACTION_PROMPT_TEMPLATE_MULTI.format(
            model_output=model_output,
            expected_count=expected_number_outputs,
        )
    if extraction_profile == EXTRACTION_PROFILE_SHUFFLING_LIST:
        return SHUFFLING_LIST_EXTRACTION_PROMPT_TEMPLATE.format(model_output=model_output)
    raise ValueError(f"Unsupported extraction profile: {extraction_profile}")


def extraction_result_has_value(
    extraction_result: Dict[str, Any],
    extraction_profile: str,
    expected_number_outputs: int = 1,
) -> bool:
    if extraction_profile == EXTRACTION_PROFILE_NUMBER:
        if expected_number_outputs <= 1:
            return extraction_result.get("number") is not None
        values = extraction_result.get("value")
        if not isinstance(values, list):
            return False
        if len(values) != expected_number_outputs:
            return False
        return all(isinstance(x, (int, float)) and not isinstance(x, bool) for x in values)
    if extraction_profile == EXTRACTION_PROFILE_SHUFFLING_LIST:
        return extraction_result.get("value") is not None
    return False


def extract_value_with_provider(
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
    extraction_profile: str,
    expected_number_outputs: int = 1,
) -> Dict[str, Any]:
    if extractor_model.lower() == "regex":
        return extract_with_regex(model_output, extraction_profile, expected_number_outputs)

    prompt = build_extraction_prompt(
        extraction_profile,
        model_output,
        expected_number_outputs=expected_number_outputs,
    )
    extractor_client = client
    extractor_provider = extractor_api_provider
    extractor_uses_completions = use_completion_endpoint(extractor_provider, extractor_model)

    if extractor_api_provider and extractor_api_provider != api_provider:
        extractor_client = build_client(extractor_api_provider, extractor_api_key)
        extractor_provider = extractor_api_provider
        extractor_uses_completions = use_completion_endpoint(extractor_provider, extractor_model)
    else:
        extractor_provider = api_provider

    if extractor_uses_completions:
        call_params = build_prompt_call_params(
            api_provider=extractor_provider,
            model=extractor_model,
            prompt=prompt,
            temperature=extraction_temperature,
            max_tokens=extraction_max_tokens,
        )
    else:
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
        response = (
            create_text_completion_with_retry(
                client=extractor_client,
                call_params=call_params,
                max_retries=max_retries,
                retry_base_sleep=retry_base_sleep,
                context_label=f"value extraction ({extractor_model}, profile={extraction_profile})",
            )
            if extractor_uses_completions
            else create_chat_completion_with_retry(
                client=extractor_client,
                call_params=call_params,
                max_retries=max_retries,
                retry_base_sleep=retry_base_sleep,
                context_label=f"value extraction ({extractor_model}, profile={extraction_profile})",
            )
        )
        result_text = get_generated_text(response, extractor_uses_completions)
        parsed = parse_extractor_json(
            result_text,
            extraction_profile=extraction_profile,
            expected_number_outputs=expected_number_outputs,
        )
        if parsed is None:
            return {"rationale": "None", "number": None, "value": None}
        return parsed
    except Exception as exc:
        print(f"Error during extraction: {exc}")
        return {"rationale": "None", "number": None, "value": None}


def build_followup_answer_only_prompt(
    original_prompt: str,
    failed_attempts: int,
    last_output: str,
    extraction_profile: str,
    expected_number_outputs: int = 1,
) -> str:
    previous_output = (last_output or "").strip()

    if extraction_profile == EXTRACTION_PROFILE_NUMBER:
        if expected_number_outputs <= 1:
            answer_instruction = (
                "That output did not contain any extractable final number. "
                "Do not explain, do not provide code, and do not add any extra text. "
                "Return only the final sampled random number as instructed."
            )
        else:
            answer_instruction = (
                f"That output did not contain {expected_number_outputs} extractable final numbers "
                "(plain numeric text, typically one number per line) as instructed. "
                "Do not explain, do not provide code, and do not add any extra text. "
                f"Return exactly {expected_number_outputs} final sampled numbers as instructed."
            )
    elif extraction_profile == EXTRACTION_PROFILE_SHUFFLING_LIST:
        answer_instruction = (
            "That output did not contain any extractable final list. "
            "Do not explain, do not provide code, and do not add any extra text. "
            "Return exactly one valid list as instructed."
        )
    else:
        answer_instruction = (
            "That output did not contain an extractable final answer. "
            "Do not explain, do not provide code, and do not add any extra text. "
            "Return only the final answer as instructed."
        )

    followup_instruction = (
        f"\n\nIMPORTANT: I have already asked you {failed_attempts} times, and your previous output was:\n"
        f"\"\"\"\n{previous_output}\n\"\"\"\"\n"
        f"{answer_instruction}"
    )

    return original_prompt + followup_instruction


def apply_prompt_find_replace(prompt_text: str, find: str, replace: str) -> str:
    if not find:
        return prompt_text
    return prompt_text.replace(find, replace)


def attach_prompt_derivatives_if_changed(
    result_item: Dict[str, Any],
    prompt_text: Any,
    after_substitution: str,
    after_model_prefix: str,
    after_model_suffix: str,
    prompt_sent_to_model: str,
) -> None:
    """Add prompt trace fields only when a stage changes the string from the previous stage."""
    if after_substitution != prompt_text:
        result_item["prompt_text_after_substitution"] = after_substitution
    if after_model_prefix != after_substitution:
        result_item["prompt_text_after_model_prefix"] = after_model_prefix
    if after_model_suffix != after_model_prefix:
        result_item["prompt_text_after_model_suffix"] = after_model_suffix
    if prompt_sent_to_model != after_model_suffix:
        result_item["prompt_text_sent_to_model"] = prompt_sent_to_model


def apply_model_prompt_prefix(model: str, prompt_text: str) -> str:
    if model == QWEN_NO_THINK_MODEL and not prompt_text.startswith(QWEN_NO_THINK_PREFIX):
        return QWEN_NO_THINK_PREFIX + prompt_text
    return prompt_text


def apply_model_prompt_suffix(model: str, prompt_text: str) -> str:
    if model in SUFFIX_MODELS:
        # avoid double-appending
        if not prompt_text.rstrip().endswith(SUFFIX_TEXT.strip()):
            return prompt_text + SUFFIX_TEXT
    return prompt_text


def use_completion_endpoint(api_provider: str, model: str) -> bool:
    return api_provider == "vllm" and model in {"meta-llama/Llama-3.2-1B"}


def build_prompt_call_params(
    api_provider: str,
    model: str,
    prompt: str,
    temperature: float,
    max_tokens: int,
    provider_order: Optional[List[str]] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "model": model,
        "prompt": prompt,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }

    if api_provider == "openrouter":
        extra_body: Dict[str, Any] = {"reasoning": {"effort": "none"}}
        if provider_order:
            extra_body["provider"] = {
                "order": provider_order,
                "allow_fallbacks": False,
                "only": provider_order,
            }
        params["extra_body"] = extra_body

    return params


def create_text_completion_with_retry(
    client: OpenAI,
    call_params: Dict[str, Any],
    max_retries: int,
    retry_base_sleep: float,
    context_label: str,
) -> Any:
    retries = max(1, max_retries)

    for attempt in range(retries):
        try:
            return client.completions.create(**call_params)
        except Exception as exc:
            msg = str(exc)
            if is_retryable_error(msg) and attempt < retries - 1:
                hinted = parse_retry_after_seconds(exc)
                if hinted is not None:
                    wait_s = min(300.0, max(0.5, hinted))
                else:
                    wait_s = min(120.0, max(0.5, retry_base_sleep) * (2 ** attempt))

                wait_s += random.uniform(0, 1)
                print(
                    f"Transient error during {context_label}; retrying in {wait_s:.1f}s "
                    f"(attempt {attempt + 1}/{retries}). Error: {msg}"
                )
                time.sleep(wait_s)
                continue
            raise

    raise RuntimeError(f"Failed after retries for {context_label}")


def get_generated_text(response: Any, use_completions: bool) -> str:
    choice = response.choices[0]
    if use_completions:
        return (getattr(choice, "text", None) or "").strip()
    return (choice.message.content or "").strip()


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

    generation_prompt_text = apply_prompt_find_replace(
        prompt_text, args.prompt_find, args.prompt_replace
    )
    after_model_prefix = apply_model_prompt_prefix(args.model, generation_prompt_text)
    after_model_suffix = apply_model_prompt_suffix(args.model, after_model_prefix)

    extraction_profile = args.extraction_profile
    extractor_model = args.value_extractor_model.strip() or args.model
    extractor_api_provider = args.value_extractor_api_provider.strip() or args.api_provider
    extractor_api_key = args.value_extractor_api_key.strip() or args.api_key
    generation_attempts = args.extraction_retries if args.extract_value else 1

    selected_output_text: Optional[str] = None
    selected_finish_reason: Optional[str] = None
    extraction_result: Dict[str, Any] = {"rationale": "None", "number": None, "value": None}
    used_generation_attempts = 0
    reinforced_prompt_used = False
    client = build_client(args.api_provider, args.api_key)

    followup_attempts = 1 if args.extract_value else 0
    total_generation_attempts = generation_attempts + followup_attempts
    generation_uses_completions = use_completion_endpoint(args.api_provider, args.model)

    last_prompt_sent_to_model = ""

    for gen_attempt in range(1, total_generation_attempts + 1):
        used_generation_attempts = gen_attempt

        current_prompt_text = after_model_suffix
        is_followup_attempt = gen_attempt > generation_attempts
        if is_followup_attempt:
            reinforced_prompt_used = True
            current_prompt_text = build_followup_answer_only_prompt(
                original_prompt=current_prompt_text,
                failed_attempts=generation_attempts,
                last_output=selected_output_text or "",
                extraction_profile=extraction_profile,
                expected_number_outputs=args.expected_number_outputs,
            )

        last_prompt_sent_to_model = current_prompt_text

        if generation_uses_completions:
            generation_call_params = build_prompt_call_params(
                api_provider=args.api_provider,
                model=args.model,
                prompt=current_prompt_text,
                temperature=args.temp,
                max_tokens=args.max_tokens,
                provider_order=provider_order,
            )
            response = create_text_completion_with_retry(
                client=client,
                call_params=generation_call_params,
                max_retries=args.max_retries,
                retry_base_sleep=args.retry_base_sleep,
                context_label=f"generation for {prompt_id}",
            )
        else:
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

        model_output = get_generated_text(response, generation_uses_completions)
        finish_reason = getattr(response.choices[0], "finish_reason", None)

        if args.verbose:
            print(f"\n--- ID: {prompt_id} (attempt {gen_attempt}/{generation_attempts}) ---\n{model_output}\n")

        selected_output_text = model_output
        selected_finish_reason = finish_reason

        if not args.extract_value:
            break

        extraction_result = extract_value_with_provider(
            model_output=model_output,
            client=client,
            api_provider=args.api_provider,
            extractor_model=extractor_model,
            extractor_api_provider=extractor_api_provider,
            extractor_api_key=extractor_api_key,
            max_retries=args.max_retries,
            retry_base_sleep=args.retry_base_sleep,
            extraction_temperature=args.value_extraction_temp,
            extraction_max_tokens=args.value_extraction_max_tokens,
            extraction_profile=extraction_profile,
            expected_number_outputs=args.expected_number_outputs,
        )

        if extraction_result_has_value(
            extraction_result,
            extraction_profile,
            expected_number_outputs=args.expected_number_outputs,
        ):
            break

        if extraction_profile == EXTRACTION_PROFILE_NUMBER and args.expected_number_outputs > 1:
            expected_label = f"{args.expected_number_outputs} numbers"
        else:
            expected_label = {
                EXTRACTION_PROFILE_NUMBER: "number",
                EXTRACTION_PROFILE_SHUFFLING_LIST: "list",
            }.get(extraction_profile, "value")

        if gen_attempt < generation_attempts:
            print(
                f"No {expected_label} extracted for prompt {prompt_id} on attempt {gen_attempt}/{generation_attempts}; retrying generation."
            )
        elif gen_attempt == generation_attempts and followup_attempts > 0:
            print(
                f"No {expected_label} extracted for prompt {prompt_id} after {generation_attempts} attempts; "
                "retrying once with reinforced answer-only instructions."
            )

    result_item = item.copy()
    attach_prompt_derivatives_if_changed(
        result_item,
        prompt_text,
        generation_prompt_text,
        after_model_prefix,
        after_model_suffix,
        last_prompt_sent_to_model,
    )
    result_item["model_output"] = selected_output_text
    result_item["model_used"] = args.model
    result_item["api_provider"] = args.api_provider
    result_item["temperature"] = args.temp
    result_item["max_tokens"] = args.max_tokens
    result_item["finish_reason"] = selected_finish_reason
    result_item["generation_attempts_used"] = used_generation_attempts
    result_item["extract_number_enabled"] = bool(args.extract_value)
    result_item["extract_value_enabled"] = bool(args.extract_value)
    result_item["reinforced_prompt_used"] = reinforced_prompt_used
    result_item["extraction_profile"] = extraction_profile if args.extract_value else None
    result_item["value_extractor_model"] = extractor_model if args.extract_value else None
    result_item["number_extractor_model"] = extractor_model if args.extract_value else None
    result_item["rationale"] = extraction_result.get("rationale") if args.extract_value else None
    result_item["expected_number_outputs"] = args.expected_number_outputs
    result_item["extracted_value"] = extraction_result.get("value") if args.extract_value else None
    result_item["extracted_number"] = (
        extraction_result.get("number")
        if args.extract_value
        and extraction_profile == EXTRACTION_PROFILE_NUMBER
        and args.expected_number_outputs <= 1
        else None
    )

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


def load_existing_result_for_item(
    item: Dict[str, Any],
    output_dir: str,
    args: argparse.Namespace,
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

    if item.get("id") is not None and existing.get("id") != item.get("id"):
        print(f"Warning: existing result id mismatch for prompt {prompt_id}; reprocessing.")
        return None

    for field in RESUME_REQUIRED_FIELDS:
        if field not in existing:
            print(f"Warning: existing result for prompt {prompt_id} is missing {field}; reprocessing.")
            return None

    if args.extract_value:
        if not (existing.get("extract_value_enabled") or existing.get("extract_number_enabled")):
            print(
                f"Warning: existing result for prompt {prompt_id} is unextracted but extraction is enabled; reprocessing."
            )
            return None

        if "rationale" not in existing:
            print(
                f"Warning: existing extracted result for prompt {prompt_id} is missing rationale; reprocessing."
            )
            return None

        existing_profile = existing.get("extraction_profile")
        if existing_profile in (None, ""):
            existing_profile = EXTRACTION_PROFILE_NUMBER

        if existing_profile != args.extraction_profile:
            print(
                f"Warning: existing extraction profile mismatch for prompt {prompt_id}; reprocessing."
            )
            return None

        if args.extraction_profile == EXTRACTION_PROFILE_NUMBER:
            existing_exp = int(existing.get("expected_number_outputs", 1))
            if existing_exp != args.expected_number_outputs:
                print(
                    f"Warning: existing expected_number_outputs mismatch for prompt {prompt_id} "
                    f"({existing_exp} vs {args.expected_number_outputs}); reprocessing."
                )
                return None
            if args.expected_number_outputs <= 1:
                if "extracted_number" not in existing:
                    print(
                        f"Warning: existing numeric extraction for prompt {prompt_id} is incomplete; reprocessing."
                    )
                    return None
            else:
                ev = existing.get("extracted_value")
                if not isinstance(ev, list) or len(ev) != args.expected_number_outputs:
                    print(
                        f"Warning: existing multi-number extraction for prompt {prompt_id} is incomplete; reprocessing."
                    )
                    return None

        if args.extraction_profile == EXTRACTION_PROFILE_SHUFFLING_LIST and "extracted_value" not in existing:
            print(
                f"Warning: existing list extraction for prompt {prompt_id} is incomplete; reprocessing."
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
        provider_order = parse_provider_order(args.api_provider, args.openrouter_provider)
        data = load_input_data(args.input_file, args.limit)
        output_dir = ensure_output_dir(args.output_dir)
    except Exception as exc:
        print(f"Error during setup: {exc}")
        return

    print(
        f"Processing {len(data)} prompts using {args.api_provider} with model {args.model} "
        f"(temp={args.temp}, extract_value={args.extract_value}, extraction_profile={args.extraction_profile}, "
        f"expected_number_outputs={args.expected_number_outputs}, parallel_requests={args.parallel_requests}, "
        f"resume={args.resume})..."
    )

    indexed_results: Dict[int, Dict[str, Any]] = {}
    pending_items: List[Tuple[int, Dict[str, Any]]] = []

    if args.resume:
        for idx, item in enumerate(data):
            existing_result = load_existing_result_for_item(item, output_dir, args)
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
