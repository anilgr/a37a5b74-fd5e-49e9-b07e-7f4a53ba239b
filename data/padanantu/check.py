import json

with open('kannada_connections.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('groups.txt', 'w', encoding='utf-8') as out:
    for day in data:
        for group in day['answers']:
            gname = group['group']
            if '{' in gname:
                out.write(f"{gname}: {group['members']}\n")
