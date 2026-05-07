import json
import os
import random
import re
import time
from typing import Any, Dict, List, Optional

from openai import OpenAI


def ensure_boolean_optional_action(argparse_module: Any) -> None:
    if hasattr(argparse_module, "BooleanOptionalAction"):
        return

    class BooleanOptionalAction(argparse_module.Action):
        def __init__(
            self,
            option_strings: List[str],
            dest: str,
            default: Any = None,
            type: Any = None,
            choices: Any = None,
            required: bool = False,
            help: Optional[str] = None,
            metavar: Optional[str] = None,
        ) -> None:
            expanded_options: List[str] = []
            for option in option_strings:
                expanded_options.append(option)
                if option.startswith("--"):
                    expanded_options.append("--no-" + option[2:])
            super().__init__(
                option_strings=expanded_options,
                dest=dest,
                nargs=0,
                default=default,
                type=type,
                choices=choices,
                required=required,
                help=help,
                metavar=metavar,
            )

        def __call__(self, parser: Any, namespace: Any, values: Any, option_string: Optional[str] = None) -> None:
            setattr(namespace, self.dest, not (option_string or "").startswith("--no-"))

        def format_usage(self) -> str:
            return " | ".join(self.option_strings)

    argparse_module.BooleanOptionalAction = BooleanOptionalAction


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


def save_summary(results: List[Dict[str, Any]], output_dir: str) -> str:
    final_output = os.path.join(output_dir, "all_results.json")
    with open(final_output, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    return final_output


def make_safe_id(value: Any) -> str:
    return str(value).replace("/", "_").replace(" ", "_").replace(":", "_")


def parse_provider_order(api_provider: str, openrouter_provider: str) -> List[str]:
    if api_provider != "openrouter" or not openrouter_provider:
        return []

    provider_order = [p.strip() for p in openrouter_provider.split(",") if p.strip()]
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

    response = getattr(exc, "response", None)
    if response and hasattr(response, "headers"):
        retry_after_header = response.headers.get("Retry-After")
        if retry_after_header:
            try:
                retry_after = float(retry_after_header)
            except ValueError:
                pass

    for pattern in (
        r"retry\s+in\s+(\d+(?:\.\d+)?)s",
        r"retrydelay['\"]?[:=]\s*['\"]?(\d+(?:\.\d+)?)(?:s|sec|seconds)?",
        r"retry[- ]after[: ](\d+(?:\.\d+)?)",
    ):
        match = re.search(pattern, str(exc), flags=re.IGNORECASE)
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
        extra_body: Dict[str, Any] = {"reasoning": {"effort": "none"}}
        if provider_order:
            extra_body["provider"] = {
                "order": provider_order,
                "allow_fallbacks": False,
                "only": provider_order,
            }
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


def strip_json_fence(result_text: str) -> str:
    text = result_text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text, flags=re.IGNORECASE)
        text = re.sub(r"\s*```$", "", text)

    start = text.find("{")
    end = text.rfind("}")
    if start != -1 and end != -1 and end >= start:
        text = text[start : end + 1]
    return text

