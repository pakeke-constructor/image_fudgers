
import map_pixel


STRGTH = 4 # grayscale strength


def make_grayscale(in_color):
    '''
    Takes a color, and converts it to a grayscale color
    '''
    r,g,b,a = in_color
    avg = (r+g+b)/3 # average pixel value

    # drift pixel values towards the average, according to strength
    ct = STRGTH + 1
    r = round((r + avg*STRGTH) / ct)
    g = round((g + avg*STRGTH) / ct)
    b = round((b + avg*STRGTH) / ct)

    return (r,g,b,a)
    



def run(inpth, outpth):
    return map_pixel.map_pixel(inpth, outpth, make_grayscale)

