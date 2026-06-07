import json
from pathlib import Path

BASE = Path(__file__).parent / "Factions"

IGNORE_FOLDERS = {
    "Scripts",
    "Styles",
    "__pycache__",
    ".git"
}

def build_manifest_for_faction(faction_root: Path):
    manifest = {}

    for item in faction_root.iterdir():
        if not item.is_dir():
            continue

        if item.name in IGNORE_FOLDERS:
            continue

        txt_files = sorted(
            f.name
            for f in item.iterdir()
            if f.is_file() and f.suffix.lower() == ".txt"
        )

        if txt_files:
            manifest[item.name] = txt_files

    return manifest

def main():
    for faction_dir in BASE.iterdir():
        if not faction_dir.is_dir():
            continue

        if faction_dir.name in IGNORE_FOLDERS:
            continue

        manifest = build_manifest_for_faction(faction_dir)

        if not manifest:
            continue

        output_path = faction_dir / "manifest.json"

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=4)

        print(f"Generated {output_path}")