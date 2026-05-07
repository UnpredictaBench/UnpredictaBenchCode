import os
import sys
import json
from pathlib import Path


def load_prompt_template(template_path):
    with open(template_path, 'r', encoding='utf-8') as f:
        return f.read()


def extract_distribution_name(filename):
    name = filename.replace('.md', '').replace('_', ' ')
    return ' '.join(word.capitalize() for word in name.split())


def extract_distributions(base_path, prompt_template, prompt_title):
    distributions = []
    base_path = Path(base_path)

    def format_prompt_text(template, distribution_name, content, file_path):
        try:
            return template.format(
                distribution_name=distribution_name,
                distribution_wikipedia=content
            )
        except KeyError as exc:
            missing_key = exc.args[0] if exc.args else "<unknown>"
            raise ValueError(
                "Template format error: missing key '{key}'. "
                "If the template contains JSON or literal braces, escape them as '{{' and '}}'. "
                "Available keys: distribution_name, distribution_wikipedia."
                .format(key=missing_key)
            ) from exc
        except Exception as exc:
            raise RuntimeError("Template format error: {error}".format(error=repr(exc))) from exc
    
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith('.md'):
                file_path = Path(root) / file
                distribution_name = extract_distribution_name(file)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    relative_path = file_path.relative_to(base_path)
                    category = str(relative_path.parent)
                    
                    prompt_text = format_prompt_text(
                        prompt_template,
                        distribution_name,
                        content,
                        file_path
                    )
                    
                    distributions.append({
                        'id': f"{category}/{distribution_name}",
                        'category': category,
                        'subcategory': distribution_name,
                        'prompt_title': prompt_title,
                        'prompt_text': prompt_text
                    })
                    
                    print(f"✓ {distribution_name}")
                    
                except Exception as e:
                    print("✗ Error: {path}\n  Type: {etype}\n  Details: {details}".format(
                        path=file_path,
                        etype=type(e).__name__,
                        details=str(e)
                    ))
    
    return distributions


def main():
    if len(sys.argv) < 5:
        print("Usage: python3 prompt_gen.py <base_path> <output_file> <prompt_template_file> <prompt_title>")
        sys.exit(1)
    
    base_path = sys.argv[1]
    output_file = sys.argv[2]
    template_file = sys.argv[3]
    prompt_title = sys.argv[4]
    
    prompt_template = load_prompt_template(template_file)
    
    print("Extracting distributions...\n")
    distributions = extract_distributions(base_path, prompt_template, prompt_title)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(distributions, f, indent=2, ensure_ascii=False)
    
    print(f"\n✓ Saved {len(distributions)} distributions to {output_file}")


if __name__ == "__main__":
    main()
