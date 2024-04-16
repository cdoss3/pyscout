#! /bin/python3

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd

# Import data to dataframe

datapath = '/home/cdoss/projects/btl/datasets/sec_player_23.csv'

df = pd.read_csv(datapath)

# Scatterplot, player vs xG
# Add a secondary df, limit xG to > 0.2




x = df['xg']
y = df['name']

# plt.scatter(x, y)
# plt.show()


