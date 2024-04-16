#! /bin/python3

import argparse

parser = argparse.ArgumentParser(description='Clean Wyscout player data. Provide a .csv file to be cleaned, output file in /pyscout/datasets')

parser.add_argument('-f', '--file', help="REQUIRED -- Provide the pato the .csv file to be cleaned", default=None)

args = parser.parse_args()

print(args.file + ' Provided')
