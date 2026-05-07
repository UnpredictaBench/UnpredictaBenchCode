#!/bin/bash
set -euo pipefail

# Usage:
#   ./scripts/run_api_with_reasoning.sh INPUT_PATH MODEL PROVIDER [OPENROUTER_API_KEY]
#
# INPUT_PATH can be a questions.json file or a directory containing questions.json files.

INPUT_PATH="${1:-}"
MODEL_NAME="${2:-}"
PROVIDER_NAME="${3:-}"
OPENROUTER_KEY="${4:-${OPENROUTER_KEY:-}}"

if [ -z "$INPUT_PATH" ] || [ -z "$MODEL_NAME" ] || [ -z "$PROVIDER_NAME" ]; then
    echo "Usage: $0 INPUT_PATH MODEL PROVIDER [OPENROUTER_API_KEY]" >&2
    exit 1
fi

if [ -z "$OPENROUTER_KEY" ]; then
    echo "Error: OPENROUTER_API_KEY is required (arg 4 or env OPENROUTER_KEY)." >&2
    exit 1
fi

# Tunables via env vars
TEMPERATURE="${TEMPERATURE:-1}"
MAX_TOKENS="${MAX_TOKENS:-4096}"
MAX_ATTEMPTS="${MAX_ATTEMPTS:-100}"
NUMBERS_TARGET="${NUMBERS_TARGET:-100}"
MAX_RETRIES="${MAX_RETRIES:-5}"
RETRY_BASE_SLEEP="${RETRY_BASE_SLEEP:-5.0}"
RESUME="${RESUME:-true}"
DRY_RUN="${DRY_RUN:-false}"
OUTPUT_ROOT="${OUTPUT_ROOT:-experiments/reasoning_numbers}"
MAX_PARALLEL="${MAX_PARALLEL:-3}"

run_one() {
    local input_file="$1"
    local base_root="$2"

    local rel_path task_dir task_name model_safe output_dir
    if [ -n "$base_root" ]; then
        rel_path="${input_file#"$base_root"/}"
        task_dir="$(dirname "$rel_path")"
        task_name="${task_dir//\//__}"
    else
        task_name="$(basename "$(dirname "$input_file")")"
    fi

    model_safe="$(echo "$MODEL_NAME" | tr '/' '_' | tr '.' '_')"
    output_dir="${OUTPUT_ROOT}/${task_name}/${model_safe}"

    args=(
        --input_file "$input_file"
        --model "$MODEL_NAME"
        --provider "$PROVIDER_NAME"
        --api_key "$OPENROUTER_KEY"
        --temp "$TEMPERATURE"
        --max_tokens "$MAX_TOKENS"
        --max_attempts "$MAX_ATTEMPTS"
        --numbers_target "$NUMBERS_TARGET"
        --max_retries "$MAX_RETRIES"
        --retry_base_sleep "$RETRY_BASE_SLEEP"
        --output_dir "$output_dir"
    )

    if [ "$RESUME" = true ]; then
        args+=(--resume)
    else
        args+=(--no-resume)
    fi

    if [ "$DRY_RUN" = true ]; then
        args+=(--dry_run)
    fi

    OPENROUTER_KEY="$OPENROUTER_KEY" python scripts/api_runner_reasoning.py "${args[@]}"
}

wait_for_slot() {
    while [ "$(jobs -pr | wc -l)" -ge "$MAX_PARALLEL" ]; do
        if ! wait -n 2>/dev/null; then
            local pid
            pid="$(jobs -pr | head -n 1)"
            if [ -n "$pid" ]; then
                wait "$pid"
            fi
        fi
    done
}

if [ -f "$INPUT_PATH" ]; then
    run_one "$INPUT_PATH" ""
elif [ -d "$INPUT_PATH" ]; then
    found_any=false
    while IFS= read -r -d '' input_file; do
        found_any=true
        wait_for_slot
        run_one "$input_file" "$INPUT_PATH" &
    done < <(find "$INPUT_PATH" -type f -name 'questions.json' -print0)

    wait

    if [ "$found_any" = false ]; then
        echo "Error: no questions.json files found under directory: $INPUT_PATH" >&2
        exit 1
    fi
else
    echo "Error: input path not found: $INPUT_PATH" >&2
    exit 1
fi
