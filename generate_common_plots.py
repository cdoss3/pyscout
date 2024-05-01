#! /bin/python3

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd

# Import data to dataframe

datapath = '/home/cdoss/work/btl/datasets/sec_player_23.csv'

df = pd.read_csv(datapath)

# Scatterplot, 2 columns with conditions, condition for coloring, condition
# for labeling
#
# Add a secondary df, limit xG to > 0.2

subset = df[['xg','name']]
xg = subset[df['xg'] > 1]
xa = subset[df['xa'] > 1]

#def btl_scatter(x, y, save_destination) -> None: 
def xg_xa_by_team(dataframe, team_name):
    """
    Plot individual players' xG vs xA, then plot individual players from a 
    specific team in a different color over the top of that

    Parameters
    ----------
    dataframe
        SUPPLY A PANDAS DF OF WYSCOUT DATA WITH XG AND XA DATA
    
    team_name
        NAME OF THE TEAM TO FILTER THE SECOND PLOT BY

    Returns
    -------
    None
        OUTPUT AN .SVG FILE OF THE OUTPUT PLOT

    """
    # Filter down original dataframe, then create a third only containing a single team's players
    xg_frame = dataframe[(dataframe['xg per 90']>0.2) | (dataframe['xa per 90']>0.2)]
    team_frame = xg_frame[xg_frame['team']==team_name]
    
    # Generate the figure/axes
    fig, ax = plt.subplots()
    
    # Plot the data
    ax.plot(xg_frame['xg per 90'], xg_frame['xa per 90'], color='gray', marker='o', linestyle='')
    ax.plot(team_frame['xg per 90'], team_frame['xa per 90'], 'ro')
    
    # Assign variables for max xA and xG
    xg_max = xg_frame['xg per 90'].max()
    xa_max = xg_frame['xa per 90'].max()
    
    # Label figure and set x and y limits
    ax.set_xlabel('xG per 90')
    ax.set_ylabel('xA per 90')
    ax.set_ybound(0, xa_max + 0.05)
    ax.set_xbound(0, xg_max + 0.05)

xg_xa_by_team(df, 'Arkansas Razorbacks')
    

def btl_2var_scatter(x, y) -> None:
    pass