import json
import sys
import re

def main():
    if len(sys.argv) != 4:
        print("Usage: python process_chunk.py <start_idx> <end_idx> <translations.json>")
        sys.exit(1)

    start_idx = int(sys.argv[1])
    end_idx = int(sys.argv[2])
    translations_file = sys.argv[3]

    # Load NYT data
    with open('connections.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    chunk = data[start_idx:end_idx]

    # Load translations
    with open(translations_file, 'r', encoding='utf-8') as f:
        exact_translations = json.load(f)

    # Apply translations
    for day in chunk:
        for group in day['answers']:
            g_name = group['group']
            
            # Find match handling smart quotes
            match = exact_translations.get(g_name)
            if not match:
                for k in exact_translations.keys():
                    if k.replace('"', '').replace('”', '').replace('“', '').replace('’', "'") == g_name.replace('"', '').replace('”', '').replace('“', '').replace('’', "'"):
                        match = exact_translations[k]
                        break
                        
            if match:
                kannada_group, kannada_members_dict = match
                group['group'] = f"{g_name} {{{kannada_group}}}"
                
                new_members = []
                for member in group['members']:
                    if member in kannada_members_dict:
                        new_members.append(f"{member} {{{kannada_members_dict[member]}}}")
                    else:
                        new_members.append(member)
                group['members'] = new_members

    # Append to output file
    output_file = 'kannada_connections.json'
    with open(output_file, 'r', encoding='utf-8') as f:
        existing_data = json.load(f)
    existing_data.extend(chunk)

    # Save and format in one step
    text = json.dumps(existing_data, ensure_ascii=False, indent=4)
    pattern = re.compile(r'"members": \[\n(.*?)\n\s*\]', re.DOTALL)
    
    def replacer(m):
        inner = m.group(1)
        inner = re.sub(r'\s*\n\s*', ' ', inner).strip()
        return f'"members": [{inner}]'
        
    formatted_text = pattern.sub(replacer, text)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(formatted_text)
        
    print(f"Successfully processed and formatted days {start_idx+1} to {end_idx}!")

if __name__ == "__main__":
    main()
