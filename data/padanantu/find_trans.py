import json
import difflib

# Mapping Kannada characters to rough English equivalents for phonetic comparison
kn_to_en = {
    'ಅ': 'a', 'ಆ': 'a', 'ಇ': 'i', 'ಈ': 'i', 'ಉ': 'u', 'ಊ': 'u', 'ಋ': 'ru', 'ಎ': 'e', 'ಏ': 'e', 'ಐ': 'ai', 'ಒ': 'o', 'ಓ': 'o', 'ಔ': 'au', 'ಅಂ': 'am', 'ಅಃ': 'ah',
    'ಕ': 'k', 'ಖ': 'k', 'ಗ': 'g', 'ಘ': 'g', 'ಙ': 'ng',
    'ಚ': 'ch', 'ಛ': 'ch', 'ಜ': 'j', 'ಝ': 'j', 'ಞ': 'ny',
    'ಟ': 't', 'ಠ': 't', 'ಡ': 'd', 'ಢ': 'd', 'ಣ': 'n',
    'ತ': 't', 'ಥ': 't', 'ದ': 'd', 'ಧ': 'd', 'ನ': 'n',
    'ಪ': 'p', 'ಫ': 'f', 'ಬ': 'b', 'ಭ': 'b', 'ಮ': 'm',
    'ಯ': 'y', 'ರ': 'r', 'ಲ': 'l', 'ವ': 'v', 'ಶ': 'sh', 'ಷ': 'sh', 'ಸ': 's', 'ಹ': 'h', 'ಳ': 'l', 'ಕ್ಷ': 'ksh', 'ಜ್ಞ': 'jn',
    'ಾ': 'a', 'ಿ': 'i', 'ೀ': 'i', 'ು': 'u', 'ೂ': 'u', 'ೃ': 'ru', 'ೆ': 'e', 'ೇ': 'e', 'ೈ': 'ai', 'ೊ': 'o', 'ೋ': 'o', 'ೌ': 'au', '್': '', 'ಂ': 'm', 'ಃ': 'h',
    '೦': '0', '೧': '1', '೨': '2', '೩': '3', '೪': '4', '೫': '5', '೬': '6', '೭': '7', '೮': '8', '೯': '9'
}

def transliterate_kn_to_en(word):
    res = ""
    for char in word:
        if char in kn_to_en:
            res += kn_to_en[char]
        elif char.isascii():
            res += char.lower()
    return res

def is_transliteration(en_word, kn_word):
    en_word = en_word.lower().replace(" ", "").replace("-", "")
    kn_word_mapped = transliterate_kn_to_en(kn_word)
    
    # Calculate similarity
    similarity = difflib.SequenceMatcher(None, en_word, kn_word_mapped).ratio()
    return similarity > 0.65

with open('kannada_connections.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

transliterated_groups = []

for day in data:
    for group in day['answers']:
        gname = group['group']
        if '{' in gname:
            # Check how many members are transliterated
            trans_count = 0
            for m in group['members']:
                if '{' in m:
                    en, kn = m.split('{')
                    en = en.strip()
                    kn = kn.replace('}', '').strip()
                    if is_transliteration(en, kn):
                        trans_count += 1
            if trans_count >= 2: # If at least 2 members are transliterations
                transliterated_groups.append((gname, group['members']))

with open('transliterated.txt', 'w', encoding='utf-8') as f:
    for gname, members in transliterated_groups:
        f.write(f"{gname}: {members}\n")
