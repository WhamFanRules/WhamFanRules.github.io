from pathlib import Path
import json

BASE = Path(__file__).parent / "Factions"
PAGES_ROOT = BASE / "pages"

def make_rule_page(faction, category, filename, content):
    page_name = filename.replace(".txt", "") + ".html"

    output_dir = PAGES_ROOT / faction / category
    output_dir.mkdir(parents=True, exist_ok=True)

    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{filename}</title>
</head>
<body>

<a href="../../{faction.lower()}.html">← Back</a>

<h1>{filename.replace(".txt","")}</h1>

<pre>{content}</pre>

</body>
</html>
"""

    (output_dir / page_name).write_text(html, encoding="utf-8")

def make_faction_index(faction: str, manifest: dict):
    output_dir = PAGES_ROOT / faction
    output_dir.mkdir(parents=True, exist_ok=True)

    cards_html = ""

    for category, files in manifest.items():
        cards_html += f'<h2>{category}</h2>\n'
        cards_html += '<div class="category-grid">\n'

        for file in files:
            name = file.replace(".txt", "")
            page = f"./{category}/{name}.html"

            cards_html += f"""
            <a class="card" href="{page}">
                <div class="card-title">{name}</div>
                <div class="card-subtitle">{category}</div>
            </a>
            """

        cards_html += "</div>\n"

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{faction}</title>
    <link rel="stylesheet" href="../../Styles/styles.css">
</head>
<body>

    <h1>{faction} Army Rules & Detachments</h1>

    {cards_html}

</body>
</html>
"""

    (output_dir / f"{faction.lower()}.html").write_text(html, encoding="utf-8")
    print(f"Generated faction index: {faction.lower()}.html")

def main():
    for faction_dir in BASE.iterdir():
        if not faction_dir.is_dir():
            continue

        manifest_path = faction_dir / "manifest.json"
        if not manifest_path.exists():
            continue

        faction = faction_dir.name

        with open(manifest_path, "r", encoding="utf-8") as f:
            manifest = json.load(f)

        # 1. generate faction index page
        make_faction_index(faction, manifest)

        # 2. generate all rule pages
        for category, files in manifest.items():
            for file in files:
                txt_path = faction_dir / category / file

                if not txt_path.exists():
                    print(f"Missing file: {txt_path}")
                    continue

                content = txt_path.read_text(encoding="utf-8")

                make_rule_page(
                    faction=faction,
                    category=category,
                    filename=file,
                    content=content
                )

    print("All pages generated successfully!")