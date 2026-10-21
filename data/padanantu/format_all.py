import re
import sys

def format_file(file_path):
    print(f"Formatting {file_path}...")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()

        pattern = re.compile(r'"members": \[\n(.*?)\n\s*\]', re.DOTALL)

        def replacer(m):
            inner = m.group(1)
            # Remove newlines and collapse extra whitespace
            inner = re.sub(r'\s*\n\s*', ' ', inner).strip()
            return f'"members": [{inner}]'

        new_text = pattern.sub(replacer, text)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_text)
        print(f"Successfully formatted {file_path}")
    except Exception as e:
        print(f"Error formatting {file_path}: {e}")

files_to_format = [
    'connections.json',
    'kannada_connections.json',
    'custom_kannada_games.json'
]

for file in files_to_format:
    format_file(file)
