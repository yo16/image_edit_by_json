# from PIL import Image


def apply_change_size(img, params):
    w = params["size"]["width"]
    h = params["size"]["height"]
    return img.resize((w, h))
