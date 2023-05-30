
from PIL import Image



FILE_NAME = ".png"


def mapp(func, im, out):
    pixels = im.load()

    w,h = im.size # pixel dims
    for x in range(w):
        for y in range(h):
            col = func(pixels[x,y])
            im.putpixel((x,y), col)
    im.save(out)


def map_pixel(inn, out, func):
    with Image.open(inn) as im:
        mapp(func, im, out)


