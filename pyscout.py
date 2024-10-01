#! /bin/python3

import matplotlib
from matplotlib import pyplot as plt
import sqlite3 as sql
import polars as pl
import pandas as pd
from os import path

def data_clean(df) -> list:
    """Rename the columns for a dataframe object build from Wyscout Adv. Search player data"""
    column_list = []

    df.rename(columns = {
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

    for column in df.columns:
        column_list.append(column)

    return column_list


def xlsx_to_csv(xlsx_file: str, output_dir: str, savefile_name: str) -> bool:
    """xlsx_to_csv(/home/[user]/.../[xl file].xlsx, /home/save/path/, 'filename.csv')
    Outputs a csv file in target directory."""

    df = pd.read_excel(xlsx_file)
    #df = pl.read_excel(xlsx_file)
    data_clean(df)

    df.to_csv(path.join(output_dir, savefile_name))
    
    # Later on, I'd like to change this to return True/False depending on
    # whether the file was saved and exists in the expected directory.
    return True


