lines=open('C:/Users/anilg/development/My Projects/vibecoding/word_puzzles/connections/suspicious.txt', encoding='utf-8').read().splitlines()
grps = {}
for l in lines:
  if '|' not in l: continue
  g = l.split('|')[0].replace('Grp:', '').strip()
  grps[g] = grps.get(g, []) + [l.split('|')[1].strip()]
res = []
for g, items in grps.items():
  res.append(g + ': ' + ', '.join(items))
open('C:/Users/anilg/development/My Projects/vibecoding/word_puzzles/connections/grouped_suspicious.txt', 'w', encoding='utf-8').write('\n'.join(res))
