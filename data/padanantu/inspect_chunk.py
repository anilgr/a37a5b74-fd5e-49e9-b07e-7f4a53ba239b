import json

with open(r'C:\Users\anilg\development\My Projects\vibecoding\word_puzzles\connections\kannada_connections.json', encoding='utf-8') as f:
    k = json.load(f)
with open(r'C:\Users\anilg\development\My Projects\vibecoding\word_puzzles\connections\connections.json', encoding='utf-8') as f:
    c = json.load(f)

print(f"kannada count: {len(k)}")
print(f"connections total: {len(c)}")
if k:
    print(f"Last date in kannada: {k[-1]['date']}")
start_idx = len(k)
end_idx = min(start_idx + 18, len(c))
print(f"Next chunk: slice [{start_idx}:{end_idx}]")

chunk = c[start_idx:end_idx]
for i, day in enumerate(chunk):
    print(f"\n--- Day {start_idx + i + 1} (Date: {day['date']}, ID: {day.get('id')}) ---")
    for g in day['answers']:
        print(f"  [{g['level']}] {g['group']}: {', '.join(g['members'])}")
