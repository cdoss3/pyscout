#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
For testing random things
"""

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd

# Import data to dataframe

datapath = '/home/cdoss/work/btl-data/datasets/sec_player_23.csv'

df = pd.read_csv(datapath)
df = df[df['minutes']>400]

player = df.loc[df['name'] == 'C. Lallier']

print(player['minutes'] + 90)