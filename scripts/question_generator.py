import json
import re
import sys
from pathlib import Path


def extract_json_from_markdown(text):
    matches = re.findall(r'```json\s*(.*?)\s*```', text, re.DOTALL)
    if matches:
        try:
            return json.loads(matches[0])
        except json.JSONDecodeError:
            return None
    
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return None


def process_results(input_file, output_file, error_file, prepend_text, extract_key):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    output = []
    errors = []
    
    for item in data:
        parsed = extract_json_from_markdown(item.get('model_output', ''))
        
        if parsed and extract_key in parsed:
            output.append({
                "id": item.get('id', ''),
                "category": item.get('category', ''),
                "subcategory": item.get('subcategory', ''),
                "prompt_title": item.get('prompt_title', ''),
                "prompt_text": (prepend_text + "\n" if prepend_text != "" else "") + parsed.get(extract_key, '')
            })
        else:
            errors.append({
                "id": item.get('id', ''),
                "category": item.get('category', ''),
                "subcategory": item.get('subcategory', ''),
                "prompt_title": item.get('prompt_title', ''),
                "model_output": item.get('model_output', '')
            })
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    
    with open(error_file, 'w', encoding='utf-8') as f:
        json.dump(errors, f, indent=2, ensure_ascii=False)
    
    print("Processed {} entries -> {}".format(len(output), output_file))
    print("Found {} errors -> {}".format(len(errors), error_file))


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage: python3 extract_questions.py <input_json_path> <prepend_text> <extract_key>")
        sys.exit(1)
    
    input_path = Path(sys.argv[1])
    prepend_text = sys.argv[2]
    extract_key = sys.argv[3]
    
    output_path = input_path.parent / ('questions.json')
    error_path = input_path.parent / ('errors.json')
    
    if input_path.exists():
        process_results(input_path, output_path, error_path, prepend_text, extract_key)
    else:
        print("Error: File not found: {}".format(input_path))
        sys.exit(1)
