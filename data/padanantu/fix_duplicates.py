import json

file_path = "kannada_connections.json"
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

for game in data:
    for answer in game['answers']:
        group = answer['group']
        members = answer['members']
        
        if group == "SUMMARY {ಸಾರಾಂಶ}":
            new_members = []
            for m in members:
                if m == "ABSTRACT {ಅಬ್ಸ್ಟ್ರಾಕ್ಟ್}": new_members.append("ABSTRACT {ಸಾರ}")
                elif m == "BRIEF {ಬ್ರೀಫ್}": new_members.append("BRIEF {ಸಂಕ್ಷಿಪ್ತ}")
                elif m == "DIGEST {ಡೈಜೆಸ್ಟ್}": new_members.append("DIGEST {ಸಂಗ್ರಹ}")
                elif m == "OUTLINE {ಔಟ್‌ಲೈನ್}": new_members.append("OUTLINE {ವಿವರಣೆ}")
                else: new_members.append(m)
            answer['members'] = new_members

        elif group == "MUSICAL INSTRUMENTS {ಸಂಗೀತ ವಾದ್ಯಗಳು}":
            new_members = []
            for m in members:
                if m == "BASS {ಬಾಸ್}": new_members.append("BASS {ತಬಲ}")
                elif m == "HARP {ಹಾರ್ಪ್}": new_members.append("HARP {ವೀಣೆ}")
                elif m == "HORN {ಹಾರ್ನ್}": new_members.append("HORN {ಕೊಂಬು}")
                elif m == "ORGAN {ಆರ್ಗನ್}": new_members.append("ORGAN {ಹಾರ್ಮೋನಿಯಂ}")
                else: new_members.append(m)
            answer['members'] = new_members

        elif group == "BIRDS {ಪಕ್ಷಿಗಳು}":
            new_members = []
            for m in members:
                if m == "CARDINAL {ಕಾರ್ಡಿನಲ್}": new_members.append("CARDINAL {ಗುಬ್ಬಚ್ಚಿ}")
                elif m == "JAY {ಜೇ}": new_members.append("JAY {ಪಾರಿವಾಳ}")
                elif m == "LARK {ಲಾರ್ಕ್}": new_members.append("LARK {ಗೂಬೆ}")
                elif m == "SWIFT {ಸ್ವಿಫ್ಟ್}": new_members.append("SWIFT {ಮರಕುಟಿಗ}")
                else: new_members.append(m)
            answer['members'] = new_members

        elif group == "WOODWINDS {ಊದುವ ವಾದ್ಯಗಳು}":
            new_members = []
            for m in members:
                if m == "CLARINET {ಕ್ಲಾರಿನೆಟ್}": new_members.append("CLARINET {ಶಹನಾಯ್}")
                elif m == "SAXOPHONE {ಸ್ಯಾಕ್ಸೋಫೋನ್}": new_members.append("SAXOPHONE {ಶಂಖ}")
                else: new_members.append(m)
            answer['members'] = new_members

        elif group == "CRITICIZE {ಟೀಕಿಸು}":
            new_members = []
            for m in members:
                if m == "KNOCK {ನಾಕ್}": new_members.append("KNOCK {ಜರೆ}")
                elif m == "PAN {ಪ್ಯಾನ್}": new_members.append("PAN {ಬೈಯು}")
                else: new_members.append(m)
            answer['members'] = new_members

        elif group == "BRIEF MOMENT {ಕ್ಷಣ}":
            new_members = []
            for m in members:
                if m == "JIFF {ಜಿಫ್}": new_members.append("JIFF {ಕ್ಷಣ}")
                elif m == "JIFFY {ಜಿಫಿ}": new_members.append("JIFFY {ಕ್ಷಣ}")
                elif m == "SECOND {ಸೆಕೆಂಡ್}": new_members.append("SECOND {ಸೆಕೆಂಡು}")
                else: new_members.append(m)
            answer['members'] = new_members

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
