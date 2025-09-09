import os
import json

# Define the base directory and the new start date
base_dir = r'c:\Users\anilg\development\my_projects\wordle_ionic\daily-challenge-words-server\pagoodu'
new_start_date = "2025/03/12"

# Walk through the directory structure
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.json'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r+', encoding='utf-8') as f:
                data = json.load(f)
                data['startDate'] = new_start_date
                f.seek(0)
                json.dump(data, f, ensure_ascii=False, indent=4)
                f.truncate()

print("All startDate fields have been updated.")