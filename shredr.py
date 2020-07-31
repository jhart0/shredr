import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", required=True, help="input filename")
parser.add_argument("-d", "--delimiter", required=True, help="delimeter to split input by")
parser.add_argument("-t", "--output_type", required=True, help="output file type")

args = parser.parse_args()

with open(args.file, 'r') as f:
    data = f.read()

dataBlocks = data.split(args.delimiter)

i = 0
name = ''
for block in dataBlocks:
    if i != 0:
        if i % 2 == 0:
            with open(name + '.' + args.output_type, 'w') as f:
                f.write(block)
        else:
            name = block
    i = i + 1

        