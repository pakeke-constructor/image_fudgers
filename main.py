
import argparse


parser = argparse.ArgumentParser(description='Process some integers.')


supported_ops = [
    "4x4_split"
]

parser.add_argument(
    'type', 
    help = 'The type of operation to do.',
    choices = supported_ops
)


args = parser.parse_args()



import atlas_gen
import os


def apply(inn, out):
    if args.type == "4x4_split":
        atlas_gen.run(inn, out)


INPUT_PTH = "_input_"
OUTPUT_PTH = "_output_"

SEP = "/"

def apply_to_all(pth, func):
    if os.path.isdir(pth):
        for p in os.listdir(pth):
            apply_to_all(pth + SEP + p, func)
    else:
        out = pth.replace(INPUT_PTH, OUTPUT_PTH)
        func(pth, out)


def get_input():
    return os.getcwd() + SEP + INPUT_PTH


apply_to_all(get_input(), apply)

