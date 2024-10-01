#! /bin/python3

import argparse
import os
import polars as pl
import matplotlib as mpl
from matplotlib import pyplot as plt
import pyscout


def main():
    running = True

    print("Welcome to pyscout!")
    print("This is an early debug version")
    print()
    print(("Select an option from the menu below by typing the corresponding "
        "number"))
    print()
    print("(1) Clean an Adv. Player search into a csv file")
    print("(2) Generate a scatterplot based on two columns")
    print()

    while running:
        choice = input("pyscout >> ")

        match choice:
            case "1":
                print()
                print(f"You chose {choice}")
                print()
                print('Calling pyscout.data_clean takes three inputs:')
                print(("    1. The full absolute path to the xlsx file you'd like "
                    "cleaned"))
                print(("    2. The absolute path to the directory you'd like to "
                      "save the csv file"))
                print(("    3. The name of the csv file itself"))
                print()
                xlsx = input("xlsx file: ")
                save_dir = input("Save file directory: ")
                filename = input("csv file name: ")
                if pyscout.xlsx_to_csv(xlsx, save_dir, filename):
                    print("We made it. Should be a csv file somewhere")
                    running = False
                else:
                    print("Not a valid choice, try again")
            case "2":
                print("In the future, this will generate plots of data")
                print("For now, it quits the loop!")
                running = False
            case _:
                print("Not a valid choice! Try again")



if __name__ == "__main__":

    main()
