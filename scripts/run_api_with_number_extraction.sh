#!/bin/bash

# Example script to run api_runner.py with OpenRouter and vLLM APIs
# This script includes numeric extraction with retry logic for outputs without numbers
# Usage: ./run_api_with_extraction.sh INPUT_PATH [OPENROUTER_API_KEY] [VLLM_API_KEY] [EXTRACTOR_MODE] [EXTRA_ARGS...]
# EXTRACTOR_MODE: llm (default) or regex
#
# Optional env (passed to api_runner.py as --prompt_find / --prompt_replace):
#   PROMPT_FIND              If set, every occurrence is replaced in each prompt before the model call.
#   PROMPT_REPLACE           Replacement string (default empty; use for deletion or substitution).
#   OUTPUT_DIR_SUFFIX        Required when PROMPT_FIND is set. Appended to the output path as
#                            .../temp_<TEMP>_<SUFFIX>/run_<N> (must not contain '/').
#   EXPECTED_NUMBER_OUTPUTS  How many numeric answers extraction expects (default 10 here; regex: one number per non-empty line).

INPUT_PATH="${1:-}"
OPENROUTER_KEY="${2:-${OPENROUTER_KEY:-}}"
VLLM_KEY="${3:-${VLLM_KEY:-vllm}}"
EXTRACTOR_MODE="${4:-${EXTRACTOR_MODE:-llm}}"

# Capture any extra args (from $5 onward) and forward to the python runner
EXTRA_ARGS=("${@:5}")

expected_result_count() {
    local input_file="$1"

    if [ ! -f "$input_file" ]; then
        echo "Error: input file not found: $input_file" >&2
        return 1
    fi

    if ! command -v jq >/dev/null 2>&1; then
        echo "Error: jq is required for resume checks." >&2
        return 1
    fi

    local total_count
    total_count=$(jq -r 'length' "$input_file") || return 1

    if [ -n "$LIMIT" ]; then
        if [ "$LIMIT" -lt "$total_count" ]; then
            echo "$LIMIT"
        else
            echo "$total_count"
        fi
    else
        echo "$total_count"
    fi
}

run_is_successful() {
    local output_dir="$1"
    local expected_count="$2"
    local summary_file="${output_dir}/all_results.json"

    if [ ! -f "$summary_file" ]; then
        return 1
    fi

    jq -e --argjson expected "$expected_count" '
        type == "array"
        and length == $expected
        and all(
            .[];
            type == "object"
            and ((.model_output // "") != "")
            and (.finish_reason != null)
        )
    ' "$summary_file" >/dev/null
}

# api_runner.py arguments exposed by this wrapper
PARALLEL_REQUESTS="${PARALLEL_REQUESTS:-40}"
# Retries transient API failures for both generation and extraction requests.
MAX_RETRIES="${MAX_RETRIES:-5}"
RETRY_BASE_SLEEP="${RETRY_BASE_SLEEP:-5.0}"
LIMIT="${LIMIT:-}"
VERBOSE="${VERBOSE:-false}"
RESUME="${RESUME:-true}"
PROMPT_FIND="${PROMPT_FIND:-"provide one valid sampled value. Return only the final sampled number as plain text:"}"
PROMPT_REPLACE="${PROMPT_REPLACE:-"provide 35 independently sampled valid values. Return only the 35 sampled numbers as plain text, one per line:"}"
OUTPUT_DIR_SUFFIX="${OUTPUT_DIR_SUFFIX:-"sampled_35_numbers"}"
# Must match the number of numeric answers in the model output (LLM extractor + regex).
EXPECTED_NUMBER_OUTPUTS="${EXPECTED_NUMBER_OUTPUTS:-35}"
# Default extractor token budget scales with EXPECTED_NUMBER_OUTPUTS unless overridden.
NUMBER_EXTRACTION_MAX_TOKENS="${NUMBER_EXTRACTION_MAX_TOKENS:-$(( 128 + (EXPECTED_NUMBER_OUTPUTS - 1) * 40 ))}"

EXTRACT_NUMBER=true
# Retries the generation step when the extractor cannot find a number.
NUMBER_EXTRACTION_RETRIES=5
NUMBER_EXTRACTION_TEMP=0.3
OPENROUTER_EXTRACTOR_MODEL="${OPENROUTER_EXTRACTOR_MODEL:-openai/gpt-4o-mini}"
OPENROUTER_EXTRACTOR_API_PROVIDER="${OPENROUTER_EXTRACTOR_API_PROVIDER:-openrouter}"
OPENROUTER_EXTRACTOR_API_KEY="${OPENROUTER_EXTRACTOR_API_KEY:-$OPENROUTER_KEY}"
VLLM_EXTRACTOR_MODEL="${VLLM_EXTRACTOR_MODEL:-}"
VLLM_EXTRACTOR_API_PROVIDER="${VLLM_EXTRACTOR_API_PROVIDER:-}"
VLLM_EXTRACTOR_API_KEY="${VLLM_EXTRACTOR_API_KEY:-}"

case "${EXTRACTOR_MODE,,}" in
    regex)
        OPENROUTER_EXTRACTOR_MODEL="regex"
        OPENROUTER_EXTRACTOR_API_PROVIDER=""
        OPENROUTER_EXTRACTOR_API_KEY=""
        VLLM_EXTRACTOR_MODEL="regex"
        VLLM_EXTRACTOR_API_PROVIDER=""
        VLLM_EXTRACTOR_API_KEY=""
        ;;
    llm)
        ;;
    *)
        echo "Error: invalid EXTRACTOR_MODE '$EXTRACTOR_MODE'. Use 'llm' or 'regex'." >&2
        exit 1
        ;;
esac


# NON-REASONING

# Meta LLama: 3.1-8B**, 3.2-1B**, 3.3-70B**
# Qwen: 3.5 35B**, 3.5 27B, 3.5 397B**
# OpenAI GPT: 4o**, 5.4**, 5.4 mini
# Anthropic: Claude Sonnet 4.6**, Opus 4.6
# XAI: Grok 4.1 Fast**
# AllenAI: olmo-3-7b-instruct**,  Olmo 3.1 32B Instruct?
# Mistral: Mistral Large 3 2512?, Mistral Small 4?, mistral-3b-2512**
# Nvidia: nemotron-3-nano-30b-a3b, nemotron-3-super-120b-a12b**
# Microsoft: Phi-4*, Phi-3.5-mini-instruct**
# Deepseek: V3.2**
# Inception: Mercury-2**


# REASONING

# Qwen: ?
# Deepseek: ?
# OpenAI: ?
# Anthropic: ?
# XAI: ?
# AllenAI: ?
# Mistral: ?
# Nvidia: ?
# Microsoft: ?
# Other vendors (Minimax, MoonshotAI, Z.ai, Deepseek, bytedance, etc.): ?


VLLM_MODELS=(
    # "microsoft/Phi-3.5-mini-instruct"
    # "allenai/Olmo-3-7B-Instruct"
    # "mistralai/Ministral-3-3B-Instruct-2512"
    # "mistralai/Ministral-3-3B-Base-2512"
    # "meta-llama/Llama-3.2-1B-Instruct"
    # "meta-llama/Llama-3.1-8B"
    # "Qwen/Qwen3.5-2B-Base"
    # "Qwen/Qwen3.5-2B"
    # "alpindale/Llama-3.2-1B"
    # "meta-llama/Llama-3.2-1B"
    )

# OpenRouter models with per-model provider order
declare -A OR_MODELS_PROVIDERS=(
    # ["inception/mercury-2"]="inception"
    # ["liquid/lfm-2.5-1.2b-instruct:free"]="liquid"
    # ["liquid/lfm-2.2-6b"]="liquid"
    # ["liquid/lfm2-8b-a1b"]="liquid"
    # ["liquid/lfm-2-24b-a2b"]="together"
    # ["meta-llama/llama-3.2-3b-instruct"]="cloudflare"
    # ["meta-llama/llama-3.1-8b-instruct"]="groq"
    # ["qwen/qwen3-4b:free"]="venice/fp8"
    # ["qwen/qwen3-8b"]="atlas-cloud/fp8"
    # ["qwen/qwen3-14b"]="deepinfra/fp8"
    # ["qwen/qwen3-30b-a3b-instruct-2507"]="alibaba" #"atlas-cloud/bf16"
    # ["qwen/qwen3-32b"]="groq" #"deepinfra/fp8"
    # ["qwen/qwen3.5-27b"]="alibaba"
    # ["qwen/qwen3.5-35b-a3b"]="alibaba"
    # ["qwen/qwen3.5-122b-a10b"]="alibaba"
    # ["qwen/qwen3.5-397b-a17b"]="alibaba"
    # ["mistralai/ministral-3b-2512"]="mistral"
    # ["allenai/olmo-3-7b-instruct"]="parasail/bf16"
    # ["qwen/qwen3-next-80b-a3b-instruct:free"]="venice/beta"
    # ["meta-llama/llama-3.1-70b-instruct"]="deepinfra/base"
    # ["openai/gpt-5.2"]="openai"
    # ["openai/gpt-5.4"]="openai"
    # ["openai/gpt-4o"]="openai"
    # ["openai/gpt-4o-mini"]="openai"
    # ["openai/gpt-4.1"]="openai"
    # ["openai/gpt-4.1-nano"]="openai"
    # ["openai/gpt-5.2-chat"]="openai"
    # ["anthropic/claude-sonnet-4.6"]="anthropic"
    # ["anthropic/claude-opus-4.6"]="anthropic"
    # ["x-ai/grok-4.1-fast"]="xai"
    ["nvidia/nemotron-3-super-120b-a12b"]="deepinfra/bf16"
    # ["deepseek/deepseek-v3.2"]="novita/fp8"
    # ["nvidia/nemotron-3-nano-30b-a3b"]="deepinfra/fp4"
    # ["mistralai/mistral-large-2512"]="mistral"
)
# declare -A OR_MODELS_PROVIDERS=()

# TEMPS=(1.0 1.5 1.8 2.0)
# TEMPS=(0.1 0.7 1.0 1.2 1.5)
TEMPS=(1.0)
MAX_TOKENS=2512 #2512 #640
RUNS=3 #3 #10

run_api_batch() {
    local input_file="$1"
    local api_provider="$2"
    local model="$3"
    local api_key="$4"
    local output_prefix="$5"
    local temp="$6"
    local run_idx="$7"
    local provider_order="${8:-}"
    local extractor_model="${9:-}"
    local extractor_api_provider="${10:-}"
    local extractor_api_key="${11:-}"
    local expected_count="${12:-}"

    local model_name output_base output_dir
    local -a runner_args

    model_name=$(echo "$model" | tr '/' '_' | tr '.' '_')
    output_base=$(basename "$(dirname "$input_file")")
    local temp_dir_segment="temp_${temp}"
    if [ -n "$PROMPT_FIND" ]; then
        temp_dir_segment="temp_${temp}_${OUTPUT_DIR_SUFFIX}"
    fi
    output_dir="experiments_${EXTRACTOR_MODE}/number_extracted/${output_base}/${output_prefix}_${model_name}/${temp_dir_segment}/run_${run_idx}"

    if [ -n "$expected_count" ] && run_is_successful "$output_dir" "$expected_count"; then
        echo "Skipping completed run: ${output_dir}"
        return 0
    fi

    runner_args=(
        --input_file "$input_file"
        --api_provider "$api_provider"
        --model "$model"
        --api_key "$api_key"
        --temp "$temp"
        --max_tokens "$MAX_TOKENS"
        --parallel_requests "$PARALLEL_REQUESTS"
        --max_retries "$MAX_RETRIES"
        --retry_base_sleep "$RETRY_BASE_SLEEP"
        --output_dir "$output_dir"
        --extraction_profile number
        $([ "$EXTRACT_NUMBER" = true ] && echo --extract_value || echo --no-extract_value)
        --extraction_retries "$NUMBER_EXTRACTION_RETRIES"
        --value_extraction_temp "$NUMBER_EXTRACTION_TEMP"
        --value_extraction_max_tokens "$NUMBER_EXTRACTION_MAX_TOKENS"
        --value_extractor_model "$extractor_model"
        --expected_number_outputs "$EXPECTED_NUMBER_OUTPUTS"
    )

    if [ -n "$extractor_api_provider" ]; then
        runner_args+=(--value_extractor_api_provider "$extractor_api_provider")
    fi

    if [ -n "$extractor_api_key" ]; then
        runner_args+=(--value_extractor_api_key "$extractor_api_key")
    fi

    if [ -n "$LIMIT" ]; then
        runner_args+=(--limit "$LIMIT")
    fi

    if [ "$VERBOSE" = true ]; then
        runner_args+=(--verbose)
    fi

    if [ "$RESUME" = true ]; then
        runner_args+=(--resume)
    else
        runner_args+=(--no-resume)
    fi

    if [ "$api_provider" = "openrouter" ]; then
        if [ -z "$provider_order" ]; then
            echo "Error: missing provider order for model '$model'. Set OR_MODELS_PROVIDERS[...]."
            exit 1
        fi
        runner_args+=(--openrouter_provider "$provider_order")
    fi

    if [ -n "$PROMPT_FIND" ]; then
        runner_args+=(
            --prompt_find "$PROMPT_FIND"
            --prompt_replace "$PROMPT_REPLACE"
            --output_dir_suffix "$OUTPUT_DIR_SUFFIX"
        )
    fi

    python3 scripts/api_runner.py "${runner_args[@]}" "${EXTRA_ARGS[@]}"
}

run_for_input_file() {
    local input_file="$1"
    local expected_count

    expected_count="$(expected_result_count "$input_file")"

    # Run OpenRouter models
    for model in "${!OR_MODELS_PROVIDERS[@]}"; do
        for temp in "${TEMPS[@]}"; do
            for ((run_idx = 1; run_idx <= RUNS; run_idx++)); do
                run_api_batch \
                    "$input_file" \
                    openrouter \
                    "$model" \
                    "$OPENROUTER_KEY" \
                    openrouter \
                    "$temp" \
                    "$run_idx" \
                    "${OR_MODELS_PROVIDERS[$model]}" \
                    "$OPENROUTER_EXTRACTOR_MODEL" \
                    "$OPENROUTER_EXTRACTOR_API_PROVIDER" \
                    "$OPENROUTER_EXTRACTOR_API_KEY" \
                    "$expected_count"
            done
        done
    done

    # Run vLLM models
    for model in "${VLLM_MODELS[@]}"; do
        for temp in "${TEMPS[@]}"; do
            for ((run_idx = 1; run_idx <= RUNS; run_idx++)); do
                run_api_batch \
                    "$input_file" \
                    vllm \
                    "$model" \
                    "$VLLM_KEY" \
                    vllm \
                    "$temp" \
                    "$run_idx" \
                    "" \
                    "$VLLM_EXTRACTOR_MODEL" \
                    "$VLLM_EXTRACTOR_API_PROVIDER" \
                    "$VLLM_EXTRACTOR_API_KEY" \
                    "$expected_count"
            done
        done
    done
}

if [ -n "$PROMPT_FIND" ]; then
    if [ -z "$OUTPUT_DIR_SUFFIX" ]; then
        echo "Error: OUTPUT_DIR_SUFFIX is required when PROMPT_FIND is set." >&2
        exit 1
    fi
    case "$OUTPUT_DIR_SUFFIX" in
        */*)
            echo "Error: OUTPUT_DIR_SUFFIX must not contain '/'." >&2
            exit 1
            ;;
    esac
fi

if [ -f "$INPUT_PATH" ]; then
    run_for_input_file "$INPUT_PATH"
elif [ -d "$INPUT_PATH" ]; then
    found_any=false
    while IFS= read -r -d '' input_file; do
        found_any=true
        run_for_input_file "$input_file"
    done < <(find "$INPUT_PATH" -type f -name 'questions.json' -print0)

    if [ "$found_any" = false ]; then
        echo "Error: no questions.json files found under directory: $INPUT_PATH" >&2
        exit 1
    fi
else
    echo "Error: input path not found: $INPUT_PATH" >&2
    exit 1
fi