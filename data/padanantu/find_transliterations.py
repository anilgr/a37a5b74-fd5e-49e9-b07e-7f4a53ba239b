import json

# Crude Kannada to Latin mapping for phonetic comparison
kannada_to_latin = {
    'ಅ': 'a', 'ಆ': 'a', 'ಇ': 'i', 'ಈ': 'i', 'ಉ': 'u', 'ಊ': 'u', 'ಋ': 'ru', 'ಎ': 'e', 'ಏ': 'e', 'ಐ': 'ai', 'ಒ': 'o', 'ಓ': 'o', 'ಔ': 'au', 'ಅಂ': 'am', 'ಅಃ': 'ah',
    'ಕ': 'k', 'ಖ': 'kh', 'ಗ': 'g', 'ಘ': 'gh', 'ಙ': 'ng',
    'ಚ': 'ch', 'ಛ': 'ch', 'ಜ': 'j', 'ಝ': 'jh', 'ಞ': 'ny',
    'ಟ': 't', 'ಠ': 'th', 'ಡ': 'd', 'ಢ': 'dh', 'ಣ': 'n',
    'ತ': 't', 'ಥ': 'th', 'ದ': 'd', 'ಧ': 'dh', 'ನ': 'n',
    'ಪ': 'p', 'ಫ': 'f', 'ಬ': 'b', 'ಭ': 'bh', 'ಮ': 'm',
    'ಯ': 'y', 'ರ': 'r', 'ಲ': 'l', 'ವ': 'v', 'ಶ': 'sh', 'ಷ': 'sh', 'ಸ': 's', 'ಹ': 'h', 'ಳ': 'l', 'ಕ್ಷ': 'ksh', 'ಜ್ಞ': 'jn',
    'ಾ': 'a', 'ಿ': 'i', 'ೀ': 'i', 'ು': 'u', 'ೂ': 'u', 'ೃ': 'ru', 'ೆ': 'e', 'ೇ': 'e', 'ೈ': 'ai', 'ೊ': 'o', 'ೋ': 'o', 'ೌ': 'au', 'ಂ': 'm', 'ಃ': 'h', '್': '',
    # zero width non joiner and joiner
    '\u200c': '', '\u200d': ''
}

def to_latin(k_str):
    res = ''
    for char in k_str:
        if char in kannada_to_latin:
            res += kannada_to_latin[char]
        else:
            # ignore unknown chars
            pass
    return res

def is_similar(eng, kan_latin):
    eng = eng.lower().replace(" ", "").replace("-", "")
    kan_latin = kan_latin.lower()
    
    # Strip vowels for a very crude consonant skeleton match
    def strip_vowels(s):
        return ''.join([c for c in s if c not in 'aeiou'])
    
    skel_eng = strip_vowels(eng)
    skel_kan = strip_vowels(kan_latin)
    
    if len(skel_eng) > 1 and skel_eng in skel_kan or skel_kan in skel_eng:
        if len(skel_kan) > 0 and len(skel_eng) / len(skel_kan) > 0.5:
            return True
    return False

d = json.load(open('C:/Users/anilg/development/My Projects/vibecoding/word_puzzles/connections/kannada_connections.json', encoding='utf-8'))
results = []
for y in d:
    for x in y['answers']:
        group_str = x['group']
        if '{' in group_str:
            eng_grp = group_str.split('{')[0].strip()
            kan_grp = group_str.split('{')[1].split('}')[0].strip()
            
            # Check members
            for mem in x['members']:
                if '{' in mem:
                    eng_mem = mem.split('{')[0].strip()
                    kan_mem = mem.split('{')[1].split('}')[0].strip()
                    
                    kan_latin = to_latin(kan_mem)
                    if is_similar(eng_mem, kan_latin):
                        results.append(f"Grp: {eng_grp} | {eng_mem} -> {kan_mem} ({kan_latin})")

open('C:/Users/anilg/development/My Projects/vibecoding/word_puzzles/connections/suspicious.txt', 'w', encoding='utf-8').write('\n'.join(results))
