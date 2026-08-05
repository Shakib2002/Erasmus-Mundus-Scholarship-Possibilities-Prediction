import json

nb_path = r'e:\ML PROJECT\Erasmus-Mundus-Scholarship-Possibilities-Prediction\notebook\2_Feature_Engineering_and_Model_Training.ipynb'
try:
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    with open('audit_2.txt', 'w', encoding='utf-8') as out:
        out.write(f"Total cells: {len(nb['cells'])}\n")
        for i, c in enumerate(nb['cells']):
            t = c['cell_type']
            s = c['source']
            if s:
                text = "".join(s)[:80].replace('\n', ' ')
            else:
                text = "EMPTY"
            out.write(f"[{i:02d}] {t.upper():<8}: {text}\n")
except Exception as e:
    print(f"Error: {e}")
