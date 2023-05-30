
import argparse
import os

import atlas_gen
import grayscale



parser = argparse.ArgumentParser(description='Process some integers.')


supported_ops = [
    "4x4_split", "grayscale"
]


parser.add_argument(
    'type', 
    help = 'The type of operation to do.',
    choices = supported_ops
)


args = parser.parse_args()





def apply(inn, out):
    if args.type == "4x4_split":
        atlas_gen.run(inn, out)
    elif args.type == "grayscale":
        grayscale.run(inn, out)


INPUT_PTH = "_input_"
OUTPUT_PTH = "_output_"

SEP = "/"

def apply_to_all(pth, func):
    if os.path.isdir(pth):
        for p in os.listdir(pth):
            apply_to_all(pth + SEP + p, func)
    else:
        outpth = pth.replace(INPUT_PTH, OUTPUT_PTH)
        os.makedirs(os.path.dirname(outpth), exist_ok=True)
        func(pth, outpth)


def get_input():
    return os.getcwd() + SEP + INPUT_PTH


def get_output():
    return os.getcwd() + SEP + OUTPUT_PTH


apply_to_all(get_input(), apply)


