# UnpredictaBench Code

This repository contains the code, prompts, and evaluation notebooks used to run and analyze the UnpredictaBench experiments. The project is organized around three main stages: preparing the data, running the model extraction pipelines, and evaluating the results.

## Setup

1. Install the Python dependencies first:

   ```bash
   pip install -r requirements.txt
   ```

2. Run the data preparation script before anything else:

   ```bash
   python prepare_data.py
   ```

   This creates the data folders used by the rest of the workflow.

## Generating Data [If you want to know how we generated the data]

The data generation flow is split between two helper modules in the `scripts/` folder:

- `scripts/question_generator.py` builds the overall question structure from the source files and model outputs.
- `scripts/prompt_generator.py` converts those questions into the final prompt format used in the dataset.

In general, the pipeline first creates or collects the raw questions, then transforms them into prompt-ready records, and finally stores the resulting JSON files for downstream use.

The distributions' information from Wikipedia is available in `distributions` directory.

## Running Experiments

Before launching any experiment, open the appropriate `.sh` file in `scripts/` and set the API key and hyperparameters there. After that, run the matching shell script.

Use these scripts depending on the task type:

- `scripts/run_api_with_number_extraction.sh` for shuffling, code, and text tasks.
- `scripts/run_api_with_realworld_extraction.sh` for real-world extraction.
- `scripts/run_api_with_reasoning.sh` for reasoning runs.

If you are running reasoning with extracting numbers from the reasoning context, use `scripts/run_api_with_realworld_extraction.sh`, otherwise use `scripts/run_api_with_number_extraction.sh` and enable change the reasoning effor in `scripts/api_runner.py` to `xhigh`.

The runner scripts call the Python execution helpers in `scripts/`, which handle API requests, retries, extraction, output folders, and resume behavior.

## Evaluation

The repository includes notebooks that walk through evaluation step by step. These notebooks are used to compute the scores and inspect the results gradually rather than in one black-box step.

Typical evaluation notebooks include:

- `get_results_acc.ipynb`
- `get_results_acc_shuffling.ipynb`
- `get_results_acc_realworld.ipynb`
- `get_results_other_metrics.ipynb`
- `get_results_other_metrics_extracted_realworld.ipynb`
- `analyze_extracted_numbers_shuffling.ipynb`

## Repository Layout

- `prepare_data.py`: downloads and writes the base data folders.
- `scripts/`: data generation, prompt generation, API runners, and helper utilities.
- `prompt_templates/`: prompt text templates used to build final prompts.
- `ground_truth_codes/` and `ground_truth_values/`: stored reference code and values.
- `*.ipynb`: notebooks for scoring, analysis, and result inspection.
- `distributions`: distributions information from Wikipedia