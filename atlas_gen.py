
from PIL import Image
import os




y_names = [
    "down", "left", "right", "up"
]

FILETYPE = ".png"



X_OFFSET = 1

def get_name(pth, x, y):
    yname = y_names[min(3,y)]
    xname = ((x + X_OFFSET) % 4) + 1
    return pth + "_" + yname + "_" + str(xname) + FILETYPE




def split_NxN(pth, im, count_x, count_y):
    '''
    splits an image into count_x * count_y portions
    '''
    imgwidth, imgheight = im.size
    step_x = round(imgwidth / count_x)
    step_y = round(imgheight / count_y)

    for x in range(0, imgwidth, step_x):
        for y in range(0, imgheight, step_y):
            box = (x, y, x+step_x, y+step_y)
            a = im.crop(box)

            i = round(x/step_x)
            j = round(y/step_y)
            a.save(get_name(pth, i, j))


IGNORE = {"die", "hit", "idle", "attack"}



def run(inpth, outpth):
    with Image.open(inpth) as im:
        for s in IGNORE:
            if s in inpth:
                return
        splt = os.path.splitext(outpth)
        pth = splt[0]
        split_NxN(pth, im, 4,4)



