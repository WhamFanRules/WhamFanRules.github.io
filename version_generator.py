from pathlib import Path
import datetime


def main():
    version = datetime.datetime.now().strftime("%Y.%m.%d.%H%M")
    Path("version.js").write_text(
        f'const VERSION = "{version}";\n',
        encoding="utf-8"
    )

    print("Generated version:", version)