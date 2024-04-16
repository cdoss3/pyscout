#! /bin/python3

import argparse

parser = argparse.ArgumentParser(description='Clean Wyscout player data. Provide a .csv file to be cleaned, output file in /pyscout/datasets')

parser.add_argument('-f', '--file', help="REQUIRED -- Provide the path to the .csv file to be cleaned", default=None)
parser.add_argument('-o', '--output', help="REQUIRED -- Provide the path to the output .csv file", default=None)

args = parser.parse_args()

with open(args.file, 'r') as file:
    lines = [line for line in file.readlines()]
    for line in lines:
        print(line)

with open(args.output, 'w') as file:
    file.write('Does this print to an output file?')

