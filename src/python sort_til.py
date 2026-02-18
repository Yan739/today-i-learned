import re

def sort_til_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # On sépare l'en-tête
    parts = re.split(r'(={60}\nTIL-\d{3})', content)
    header = parts[0]

    tils = []
    # On reconstruit chaque bloc TIL
    for i in range(1, len(parts), 2):
        til_block = parts[i] + parts[i+1]

        # Extraction de la date
        date_match = re.search(r'Date\s*:\s*(\d{4}-\d{2}-\d{2})', til_block)
        date = date_match.group(1) if date_match else "0000-00-00"

        tils.append({'date': date, 'content': til_block.strip()})

    # Tri par date
    tils.sort(key=lambda x: x['date'])

    # Réécriture du fichier
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(header.strip() + "\n\n")
        for idx, til in enumerate(tils, 1):

            content_fixed = re.sub(r'TIL-\d{3}', f'TIL-{idx:03}', til['content'])
            f.write(content_fixed + "\n\n\n")

        f.write("="*60 + "\nMODELE TIL A COPIER\n" + "="*60 + "\n...")

    print(f" {len(tils)} TIL triés et réindexés avec succès dans {filename} !")

if __name__ == "__main__":
    sort_til_file('til.txt')