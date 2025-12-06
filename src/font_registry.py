from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


FONT_FILES = {
    "default": BASE_DIR / "fonts" / "meiryo.ttc",
    "arial": BASE_DIR / "fonts" / "arial.ttf",
    "meiryo": BASE_DIR / "fonts" / "meiryo.ttc",
    "msgothic": BASE_DIR / "fonts" / "msgothic.ttc",
    "notosansjp": BASE_DIR / "fonts" / "NotoSansJP-VF.ttf",
    "yugothic": BASE_DIR / "fonts" / "YuGothR.ttc",
}


def get_font_path(name):
    key = name.lower()
    p = FONT_FILES.get(key)

    # 見つけたら返す
    if p is not None and p.exists():
        return str(p)

    # 見つからなかったらdefaultを返す
    return str(FONT_FILES.get("default"))
