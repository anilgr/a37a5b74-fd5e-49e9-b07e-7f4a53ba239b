import json
d = json.load(open('C:/Users/anilg/development/My Projects/vibecoding/word_puzzles/connections/kannada_connections.json', encoding='utf-8'))
res = []
for y in d:
    for x in y['answers']:
        res.append(x['group'] + ' -> ' + ', '.join(x['members']))
open('C:/Users/anilg/development/My Projects/vibecoding/word_puzzles/connections/all_groups.txt', 'w', encoding='utf-8').write('\n'.join(res))
