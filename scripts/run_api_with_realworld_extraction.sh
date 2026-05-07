#!/bin/bash

# Example script to run realworld_api_runner.py with OpenRouter and vLLM APIs
# Usage: ./run_api_with_realworld_extraction.sh INPUT_PATH [OPENROUTER_API_KEY] [VLLM_API_KEY] [EXTRACTOR_MODE] [EXTRA_ARGS...]
# EXTRACTOR_MODE: llm (default) or regex

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

# realworld_api_runner.py arguments exposed by this wrapper
PARALLEL_REQUESTS="${PARALLEL_REQUESTS:-30}"
MAX_RETRIES="${MAX_RETRIES:-5}"
RETRY_BASE_SLEEP="${RETRY_BASE_SLEEP:-5.0}"
LIMIT="${LIMIT:-}"
VERBOSE="${VERBOSE:-false}"
RESUME="${RESUME:-false}"
MAPPING_VALIDATE="${MAPPING_VALIDATE:-true}"
MAPPING_LENIENT="${MAPPING_LENIENT:-false}"

EXTRACT_VALUE=true
EXTRACTION_RETRIES=5
VALUE_EXTRACTION_TEMP=0.3
VALUE_EXTRACTION_MAX_TOKENS=128
OPENROUTER_EXTRACTOR_MODEL="${OPENROUTER_EXTRACTOR_MODEL:-}"
OPENROUTER_EXTRACTOR_API_PROVIDER="${OPENROUTER_EXTRACTOR_API_PROVIDER:-}"
OPENROUTER_EXTRACTOR_API_KEY="${OPENROUTER_EXTRACTOR_API_KEY:-$OPENROUTER_KEY}"
VLLM_EXTRACTOR_MODEL="${VLLM_EXTRACTOR_MODEL:-}"
VLLM_EXTRACTOR_API_PROVIDER="${VLLM_EXTRACTOR_API_PROVIDER:-}"
VLLM_EXTRACTOR_API_KEY="${VLLM_EXTRACTOR_API_KEY:-$OPENROUTER_KEY}"

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


# Non-reasoning examples (set providers in OR_MODELS_PROVIDERS below)
VLLM_MODELS=(
    # "microsoft/Phi-3.5-mini-instruct"
    # "allenai/Olmo-3-7B-Instruct"
    # "mistralai/Ministral-3-3B-Instruct-2512"
    # "mistralai/Ministral-3-3B-Base-2512"
    # "meta-llama/Llama-3.2-1B-Instruct"
    "Qwen/Qwen3.5-2B"
    )

declare -A OR_MODELS_PROVIDERS=(
    # ["openai/gpt-4o-mini"]="openai"
    # ["inception/mercury-2"]="inception"
    # ["meta-llama/llama-3.1-8b-instruct"]="groq"
    # ["meta-llama/llama-3.1-70b-instruct"]="deepinfra/base"
    # ["qwen/qwen3.5-397b-a17b"]="alibaba"
    # ["qwen/qwen3.5-35b-a3b"]="alibaba"
    # ["qwen/qwen3-32b"]="groq" #"deepinfra/fp8"
    # ["openai/gpt-5.4"]="openai"
    # ["openai/gpt-4o"]="openai"
    # ["deepseek/deepseek-v3.2"]="novita/fp8"
    # ["x-ai/grok-4.1-fast"]="xai"
    # ["nvidia/nemotron-3-super-120b-a12b"]="deepinfra/bf16"
    # ["anthropic/claude-sonnet-4.6"]="anthropic"
    # ["nvidia/nemotron-3-nano-30b-a3b"]="deepinfra/fp4"
    # ["mistralai/mistral-large-2512"]="mistral"
)   

# TEMPS=(0.7 1.0 1.2 0.1 1.5)
TEMPS=(1.0)
MAX_TOKENS=64
RUNS=100

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
    output_dir="experiments_${EXTRACTOR_MODE}/realworld_extracted/${output_base}/${output_prefix}_${model_name}/temp_${temp}/run_${run_idx}"

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
        $([ "$EXTRACT_VALUE" = true ] && echo --extract_value || echo --no-extract_value)
        --extraction_retries "$EXTRACTION_RETRIES"
        --value_extraction_temp "$VALUE_EXTRACTION_TEMP"
        --value_extraction_max_tokens "$VALUE_EXTRACTION_MAX_TOKENS"
        --value_extractor_model "$extractor_model"
        $([ "$MAPPING_VALIDATE" = true ] && echo --mapping_validate || echo --no-mapping_validate)
        $([ "$MAPPING_LENIENT" = true ] && echo --mapping_lenient || echo --no-mapping_lenient)
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
            echo "Error: missing provider order for model '$model'. Set OR_MODELS_PROVIDERS[...]." >&2
            exit 1
        fi
        runner_args+=(--openrouter_provider "$provider_order")
    fi

    python3 scripts/realworld_api_runner.py "${runner_args[@]}" "${EXTRA_ARGS[@]}"
}

run_for_input_file() {
    local input_file="$1"
    local expected_count

    expected_count="$(expected_result_count "$input_file")"

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
