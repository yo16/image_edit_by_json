from PIL import ImageDraw, ImageFont


def apply_add_text(img, params):
    draw = ImageDraw.Draw(img)
    text = params["text"]
    x = params["position"]["x"]
    y = params["position"]["y"]
    font_path = params.get("font", "Arial")
    size = params.get("font_size", 20)
    color = params.get("color", "black")
    try:
        font = ImageFont.truetype(font_path, size)
    except:
        font = ImageFont.load_default()
    draw.text((x, y), text, fill=color, font=font)
    return img

