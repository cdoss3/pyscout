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
    df.rename(columns={
        'Total actions / successful': 'Total actions',
        'Unnamed: 6': 'Successful actions',
        'Shots / on target': 'Shots',
        'Unnamed: 10': 'Shots on target',
        'Passes / accurate': 'Passes attempted',
        'Unnamed: 13': 'Passes completed',
        'Long passes / accurate': 'Long passes attempted',
        'Unnamed: 15': 'Long passes completed',
        'Crosses / accurate': 'Crosses attempted',
        'Unnamed: 17': 'Crosses completed',
        'Dribbles / successful': 'Dribbles attempted',
        'Unnamed: 19': 'Dribbles completed',
        'Duels / won': 'Duels attempted',
        'Unnamed: 21': 'Duels won',
        'Aerial duels / won': 'Aerial duels attempted',
        'Unnamed: 23': 'Aerial duels won',
        'Losses / own half': 'Lost possession',
        'Unnamed: 26': 'Lost possession in own half',
        'Recoveries / opp. half': 'Recovered ball',
        'Unnamed: 28': 'Recovered ball in opp half',
        'Defensive duels / won': 'Defensive duels',
        'Unnamed: 32': 'Defensive duels won',
        'Loose ball duels / won': 'Loose ball duels',
        'Unnamed: 34': 'Loose ball duels won',
        'Sliding tackles / successful': 'Sliding tackles attempted',
        'Unnamed: 36': 'Sliding tackles successful',
        'Offensive duels / won': 'Offensive duels attempted',
        'Unnamed: 43': 'Offensive duels won',
        'Through passes / accurate': 'Through balls attempted',
        'Unnamed: 49': 'Through balls completed',
        'Passes to final third / accurate': 'Passes to final third attempted',
        'Unnamed: 53': 'Passes to final third successful',
        'Passes to penalty area / accurate': 'Passes to penalty area attempted',
        'Unnamed: 55': 'Passes to penalty area successful',
        'Forward passes / accurate': 'Forward passes attempted',
        'Unnamed: 58': 'Forward passes completed',
        'Back passes / accurate': 'Back passes attempted',
        'Unnamed: 60': 'Back passes completed',
        'Saves / with reflexes': 'Saves',
        'Unnamed: 65': 'Reflex saves',
        'Passes to GK / accurate': 'Passes to GK attempted',
        'Unnamed: 68': 'passes to GK completed',
}, inplace=True)

data_clean(df)

# Test output column names in console

for column in df.columns:
    print(column)

# Output dataframe to .csv file

df.to_csv(args.output)
