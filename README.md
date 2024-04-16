A collection of python modules to be able to quickly clean data from Wyscout .csv files.

USAGE:

From Linux CLI:
    Consider a .xlsx file in /home/[user]/data/player_data.xlsx

    ./clean_player_data -f /home/[user]/data/player_data.xlsx -o /home/[user]/data/player_data_out.csv

    Will save a new file called "player_data_out.csv" with tidy column names, duplicates handled, etc.


TO-DO:

    - Make the script function (Import previous work from Jupyter Notebook)
    - Add config file to designate default file input and output locations
    - Add functionality for handling team data
    - Add option to automatically generate certain plots/analysis based on cli args
    - Make this back-end, add GUI front-end
