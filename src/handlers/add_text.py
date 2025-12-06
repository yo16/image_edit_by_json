from PIL import ImageDraw, ImageFont

from font_registry import get_font_path

def parse_color(col):
    if isinstance(col, str) and col.startswith("#"):
        col = col.lstrip("#")
        if len(col) == 6:
            r = int(col[0:2], 16)
            g = int(col[2:4], 16)
            h = int(col[4:6], 16)
            return (r, g, h, 255)
        if len(col) == 8:
            r = int(col[0:2], 16)
            g = int(col[2:4], 16)
            h = int(col[4:6], 16)
            a = int(col[6:8], 16)
            return (r, g, h, a)
    return col

# 縁取りを描画する
def write_frame(draw, x, y, text, font_path, font_size, stroke_width, stroke_color):
    try:
        font = ImageFont.truetype(font_path, font_size)
    except:
        print(f"Font not found: {font_path}")
        font = ImageFont.load_default()

    for dx in range(-stroke_width, stroke_width + 1):
        for dy in range(-stroke_width, stroke_width + 1):
            if dx == 0 and dy == 0:
                continue
            draw.text((x + dx, y + dy), text, fill=stroke_color, font=font, font_size=font_size)



def apply_add_text(img, params):
    draw = ImageDraw.Draw(img)
    text = params["text"]
    x = params["position"]["x"]
    y = params["position"]["y"]

    font_name = params.get("font", "default")
    font_path = get_font_path(font_name)
    size = params.get("font_size", 20)
    try:
        font = ImageFont.truetype(font_path, size)
    except:
        print(f"Font not found: {font_path}")
        font = ImageFont.load_default()

    # strokeがある場合は、widthとcolorを取得して縁取り
    stroke = params.get("stroke", None)
    if stroke:
        stroke_width = stroke.get("width", 1)
        stroke_col = stroke.get("color", "black")
        stroke_col = parse_color(stroke_col)
        write_frame(draw, x, y, text, font_path, size, stroke_width, stroke_col)

    col = params.get("color", "black")
    col = parse_color(col)
    
    draw.text((x, y), text, fill=col, font=font)
    return img

