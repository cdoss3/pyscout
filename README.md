A collection of python modules to be able to quickly clean data from Wyscout .csv files.

USAGE:

From Linux CLI:
    Consider a .xlsx file in /home/[user]/data/player_data.xlsx

    ./clean_player_data -f /home/[user]/data/player_data.xlsx -o /home/[user]/data/player_data_out.csv

    Will save a new file called "player_data_out.csv" with tidy column names, duplicates handled, etc.


TO-DO:

    - generate_common_plots to input a .csv file and output a set of common data visualizations as .png files
    - Add config file to designate default file input and output locations
    - Add functionality for handling team data
    - Add option to automatically generate certain plots/analysis based on cli args
    - GUI front-end
