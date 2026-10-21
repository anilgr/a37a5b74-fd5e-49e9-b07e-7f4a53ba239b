# NYT Connections: Kannada Adaptation Project

## 🎯 Project Goal
This project involves parsing a massive JSON archive of the NYT Connections game (`connections.json`) and translating/culturally adapting the categories and words into a Kannada and Indian context. The output is stored in `kannada_connections.json`.

## 📍 Current Progress (Where to resume)
* **Input File**: `connections.json` (contains the original English dataset).
* **Output File**: `kannada_connections.json` (contains the adapted data).
* **Progress Checkpoint**: We have successfully processed **Days 1 through 378** (total 378 days).
* **Next Action**: The next AI session should resume from **Day 379** (using list slicing `data[378:396]` in Python for the next chunk).

## 📜 Strict Formatting Rules (CRITICAL)
1. **Preserve Original Structure**: The original JSON schema (`id`, `date`, `level`, arrays, etc.) must remain 100% intact.
2. **Side-by-Side Braces Format**: All translations/adaptations must be appended directly next to the original English text using braces: `ORIGINAL {KANNADA}`. 
   * Example Group: `"NBA TEAMS {ಐಪಿಎಲ್ ತಂಡಗಳು}"`
   * Example Members: `"BUCKS {ಆರ್‌ಸಿಬಿ}", "HEAT {ಸಿಎಸ್‌ಕೆ}", "JAZZ {ಮುಂಬೈ}", "NETS {ಕೆಕೆಆರ್}"`
3. **Cultural Adaptation Over Literal Translation**: You do not have to translate words literally. Adapt them to fit the Karnataka/Kannada/Indian context (e.g., swapping US basketball teams for IPL teams, or US magazines for Kannada magazines).
4. **Skip Un-translatable Wordplay**: If a category relies heavily on English spelling, grammar, or obscure US pop culture (e.g., "CONSECUTIVE DOUBLE LETTERS" or "WORDS BEFORE DAYS OF THE WEEK"), **DO NOT** attempt to translate or adapt it. Leave the group and its members exactly as they are in plain English, without braces.

## ⚙️ Established AI Workflow
Do NOT try to write the JSON using raw LLM text generation (it causes syntax errors). Instead, follow this exact workflow:
1. **Extract**: Write a Python script to extract the next chunk of 18-20 days from `connections.json` and print the groups/members.
2. **Translate**: Generate a mapping of valid adaptations for that chunk (skipping the un-translatable ones).
3. **Script**: Write a Python script (e.g., `append_chunk.py`) that contains the dictionary mapping, iterates over the chunk, applies the `ORIGINAL {KANNADA}` formatting strictly by matching the English keys, and then `extend`s the `kannada_connections.json` file.
4. **Execute**: Run the script to append the data safely.
