#キャンバスを指定サイズに変更する
# 新サイズ < 元画像 → トリミング（左上基準）
# 新サイズ > 元画像 → 透明背景で右下に余白ができる

from PIL import Image


def apply_change_size(img, params):
    w = params["size"]["width"]
    h = params["size"]["height"]

    img = img.convert("RGBA")
    ow, oh = img.size

    cx = ow // 2
    cy = oh // 2

    left = cx - w // 2
    upper = cy - h // 2
    right = left + w
    lower = upper + h

    new_img = Image.new("RGBA", (w, h), (0, 0, 0, 0))

    if w <= ow and h <= oh:
        crop = img.crop((left, upper, right, lower))
        new_img.paste(crop, (0, 0))
        return new_img

    paste_x = max(0, -left)
    paste_y = max(0, -upper)

    crop_left = max(0, left)
    crop_upper = max(0, upper)
    crop_right = min(right, ow)
    crop_lower = min(lower, oh)

    crop = img.crop((crop_left, crop_upper, crop_right, crop_lower))
    new_img.paste(crop, (paste_x, paste_y))

    return new_img

