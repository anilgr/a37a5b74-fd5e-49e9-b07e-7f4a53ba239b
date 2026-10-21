import json

file_path = "kannada_connections.json"
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

group_counts = {}
for game in data:
    for answer in game['answers']:
        group = answer['group']
        group_counts[group] = group_counts.get(group, 0) + 1

duplicates = {k: v for k, v in group_counts.items() if v > 1 and "{" in k}

with open('dup_members.txt', 'w', encoding='utf-8') as f:
    for game in data:
        for answer in game['answers']:
            if answer['group'] in duplicates:
                f.write(f"Game {game['id']} | Group: {answer['group']}\n")
                f.write(f"  Members: {', '.join(answer['members'])}\n\n")
