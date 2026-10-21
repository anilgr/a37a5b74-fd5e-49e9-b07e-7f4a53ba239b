import json

with open('kannada_connections.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

c = 0
with open('check_snakes.txt', 'w', encoding='utf-8') as out:
    for day in data:
        for group in day['answers']:
            if 'SNAKES' in group['group']:
                c += 1
                out.write(f"{group['group']}: {group['members']}\n")
    out.write(f"Total: {c}\n")
