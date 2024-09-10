#! /bin/python3

import argparse
import pandas as pd

# Argument parser for CLI integration
# TO-DO - Add error handling for incorrect file types in input

parser = argparse.ArgumentParser(description='Clean Wyscout player data. Provide a .xlsx file to be cleaned, output .csv file in /pyscout/datasets')

parser.add_argument('-f', '--file', help="REQUIRED -- Provide the path to the .xlsx file to be cleaned", default=None)
parser.add_argument('-o', '--output', help="REQUIRED -- Provide the path to the output .csv file", default=None)

args = parser.parse_args()

# Import excel file to dataframe

df = pd.read_excel(args.file)

# Define a function to clean the column names. Then, execute the function on the dataframe.

def data_clean(df):
    df.drop(['Team', 'Weight', 'Height'], axis=1, inplace=True)
    df.columns = [x.lower().replace(', %', ' pct').replace(', m', ' (m)').replace(' / ', '/').replace('non-penalty', 'non pen') for x in df.columns]
    df.rename(columns={
        'player': 'name',
        'team within selected timeframe': 'team',
        'age': 'birth year',
        'matches played': 'appearances',
        'minutes played': 'minutes', 
        'back passes received as gk per 90': 'gk passes received',
        'aerial duels per 90.1': 'aerial duels per 90',
    }, inplace=True)

data_clean(df)

# Test output column names in console

for column in df.columns:
    print(column)

# Output dataframe to .csv file

df.to_csv(args.output)

# Print column names to .txt file for reference

with open('column_names.txt', 'w') as file:
    for column in df.columns:
        file.write(column + '\n')
