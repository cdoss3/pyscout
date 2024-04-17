#! /bin/python3

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd

# Import data to dataframe

#datapath = '/home/cdoss/projects/btl/datasets/sec_player_23.csv'

#df = pd.read_csv(datapath)

# Scatterplot, player vs xG
# Add a secondary df, limit xG to > 0.2

#subset = df[['xg','name']]
#xg = subset[subset['xg']>1]

x = np.random.randn(20)
y = np.random.randn(20)


def btl_scatter(x, y, save_destination) -> None: 
    """
    Compare two parameters. Define x and y axes, then plot them against each other

    Parameters
    ----------
    x : LIST
        DATA ASSIGNED TO THE X-AXIS
    y : LIST
        DATA ASSIGNED TO THE Y-AXIS
    save_destination: STRING
                      .PNG SAVE LOCATION AND FILE NAME  

    Returns
    -------
    None
        OUTPUT A .PNG FILE OF THE OUTPUT PLOT

    """
    plt.scatter(x, y, color='red')
    plt.show()

btl_scatter(x, y)

def btl_2var_scatter(x, y) -> None:
    pass