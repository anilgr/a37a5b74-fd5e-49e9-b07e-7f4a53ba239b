import json

file_path = "kannada_connections.json"
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

for game in data:
    for answer in game['answers']:
        group_base = answer['group'].split(' {')[0]
        members = answer['members']
        
        # 1. SLANG FOR ZERO
        if group_base == "SLANG FOR ZERO":
            new_members = []
            for m in members:
                if m == "JACK {ಜಾಕ್}": new_members.append("JACK {ಶೂನ್ಯ}")
                elif m == "SQUAT {ಸ್ಕ್ವಾಟ್}": new_members.append("SQUAT {ಖಾಲಿ}")
                elif m == "ZIP {ಜಿಪ್}": new_members.append("ZIP {ಏನೂ ಇಲ್ಲ}")
                else: new_members.append(m)
            answer['members'] = new_members

        # 2. BALDERDASH
        elif group_base == "BALDERDASH":
            new_members = []
            for m in members:
                if m == "BUNK {ಬಂಕ್}": new_members.append("BUNK {ಹುಸಿ}")
                elif m == "CROCK {ಕ್ರಾಕ್}": new_members.append("CROCK {ಕಟ್ಟುಕಥೆ}")
                elif m == "HOGWASH {ಹೋಗ್ವಾಶ್}": new_members.append("HOGWASH {ಅಸಂಬದ್ಧ}")
                elif m == "HORSEFEATHERS {ಹಾರ್ಸ್\u200cಫೆದರ್ಸ್}": new_members.append("HORSEFEATHERS {ಹುಚ್ಚಾಟ}")
                elif m == "BULL {ಬುಲ್}": new_members.append("BULL {ಸುಳ್ಳು}")
                elif m == "ROT {ರಾಟ್}": new_members.append("ROT {ಕಸ}")
                else: new_members.append(m)
            answer['members'] = new_members

        # 3. CONCEAL
        elif group_base == "CONCEAL":
            new_members = []
            for m in members:
                if m == "BLOCK {ಬ್ಲಾಕ್}": new_members.append("BLOCK {ತಡೆ}")
                elif m == "COVER {ಕವರ್}": new_members.append("COVER {ಮುಚ್ಚು}")
                elif m == "OBSCURE {ಮರೆಮಾಚು}": new_members.append("OBSCURE {ಅಡಗಿಸು}")
                else: new_members.append(m)
            answer['members'] = new_members

        # 4. EAT VORACIOUSLY
        elif group_base == "EAT VORACIOUSLY":
            new_members = []
            for m in members:
                if m == "DOWN {ಡೌನ್}": new_members.append("DOWN {ಗಬಗಬನೆ ತಿನ್ನು}")
                elif m == "SCARF {ಸ್ಕಾರ್ಫ್}": new_members.append("SCARF {ನುಂಗಿಹಾಕು}")
                else: new_members.append(m)
            answer['members'] = new_members

        # 5. MUSICAL INSTRUMENTS
        elif group_base == "MUSICAL INSTRUMENTS":
            new_members = []
            for m in members:
                if m == "BASS {ಬಾಸ್}": new_members.append("BASS {ತಬಲ}")
                elif m == "BASSOON {ಬಾಸೂನ್}": new_members.append("BASSOON {ಕೊಳಲು}")
                elif m == "HARP {ಹಾರ್ಪ್}": new_members.append("HARP {ವೀಣೆ}")
                elif m == "RECORDER {ರೆಕಾರ್ಡರ್}": new_members.append("RECORDER {ತಾಳ}")
                else: new_members.append(m)
            answer['members'] = new_members

        # 6. INSIDE INFO
        elif group_base == "INSIDE INFO":
            new_members = []
            for m in members:
                if m == "DOPE {ಡೋಪ್}": new_members.append("DOPE {ಗುಟ್ಟು}")
                elif m == "SCOOP {ಸ್ಕೂಪ್}": new_members.append("SCOOP {ಸುದ್ದಿ}")
                elif m == "SKINNY {ಸ್ಕಿನ್ನಿ}": new_members.append("SKINNY {ಮಾಹಿತಿ}")
                else: new_members.append(m)
            answer['members'] = new_members

        # 7. INTELLIGENT
        elif group_base == "INTELLIGENT":
            new_members = []
            for m in members:
                if m == "SMART {ಸ್ಮಾರ್ಟ್}": new_members.append("SMART {ಚಾಣಾಕ್ಷ}")
                else: new_members.append(m)
            answer['members'] = new_members
            
        # 8. SHOE PARTS
        elif group_base == "SHOE PARTS":
            new_members = []
            for m in members:
                if m == "EYELET {ಐಲೆಟ್}": new_members.append("EYELET {ರಂಧ್ರ}")
                elif m == "LACE {ಲೇಸ್}": new_members.append("LACE {ಹಗ್ಗ}")
                else: new_members.append(m)
            answer['members'] = new_members
            
        # 9. BOATS
        elif group_base == "BOATS":
            new_members = []
            for m in members:
                if m == "BARGE {ಬಾರ್ಜ್}": new_members.append("BARGE {ಹಡಗು}")
                elif m == "DORY {ಡೋರಿ}": new_members.append("DORY {ದೋಣಿ}")
                elif m == "SCOW {ಸ್ಕೌ}": new_members.append("SCOW {ನಾವೆ}")
                elif m == "SLOOP {ಸ್ಲೂಪ್}": new_members.append("SLOOP {ಜಲನೌಕೆ}")
                else: new_members.append(m)
            answer['members'] = new_members

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
