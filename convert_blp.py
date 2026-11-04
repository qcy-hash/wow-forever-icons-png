from pathlib import Path
from PIL import Image

source_dir = Path(".")
output_dir = Path("./png_icons")
output_dir.mkdir(exist_ok=True)

for blp_file in source_dir.glob("*.blp"):
    try:
        with Image.open(blp_file) as img:
            png_path = output_dir / f"{blp_file.stem}.png"
            img.convert("RGBA").save(png_path, "PNG")
            print(f"Converted: {blp_file.name} -> {png_path.name}")
    except Exception as e:
        print(f"Failed {blp_file.name}: {e}")