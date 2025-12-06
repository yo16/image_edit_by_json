import json
from PIL import Image

from handlers import EDIT_HANDLERS


def process_image(config_path):
    with open(config_path, "r", encoding="utf-8") as f:
        cfg = json.load(f)

    img = Image.open(cfg["source_image"])

    for edit in cfg["edit"]:
        t = edit["type"]
        handler = EDIT_HANDLERS.get(t)
        if handler:
            img = handler(img, edit)
        else:
            print(f"Unknown type: {t}")

    img.save(cfg["output_image"])
    print("Saved:", cfg["output_image"])


if __name__ == "__main__":
    process_image("materials_instructions/instruction.json")
