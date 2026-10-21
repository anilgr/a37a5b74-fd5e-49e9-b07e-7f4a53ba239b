import json

with open('kannada_connections.json', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the specific snake strings
text = text.replace('"ADDER {ಆಡರ್}", "BOA {ಬೋವಾ}", "MAMBA {ಮಾಂಬಾ}", "MOCCASIN {ಮೊಕಾಸಿನ್}"', '"ADDER {ನಾಗರಹಾವು}", "BOA {ಹೆಬ್ಬಾವು}", "MAMBA {ಕಾಳಿಂಗ ಸರ್ಪ}", "MOCCASIN {ಮಂಡಲದ ಹಾವು}"')

with open('kannada_connections.json', 'w', encoding='utf-8') as f:
    f.write(text)
