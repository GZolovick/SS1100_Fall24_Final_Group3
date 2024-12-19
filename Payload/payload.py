# %% Import Libraries----------------------------------------------------------

import pandas as pd                # used to import raw RGB files
import numpy as np                 # used to stack/combine RGB files
import matplotlib.pyplot as plt    # used for visualizations

# %% Task-1: Load Raw RGB Input Files------------------------------------------

# imports csv values using pandas
def load_csv_data(input_csv):
    output_csv = pd.read_csv(input_csv)
    return output_csv

# %% Task-2: Verify RGB Band Dimensions----------------------------------------

# verifies equal dimensions for each input csv
def dimension_verification(red, green, blue):
    if red.shape != blue.shape or red.shape != green.shape:
        False, print("ERROR: The provided RGB files do not have the same size.")
    else:
        #True, print("Dimensions are equal")
        verification = True
        return (verification)

# %% Task-3: Combine RGB Bands-------------------------------------------------

# test if dimensions of inputs are equal, then combines into one RGB image
def combine_RGB(red, green, blue):
    
    # load csv data files
    red_csv = load_csv_data(red)
    green_csv = load_csv_data(green)
    blue_csv = load_csv_data(blue)
    
    verification = dimension_verification(red_csv, green_csv, blue_csv)
    if  verification == True:
        #print("Dimensions are verified")
        RGB_image = np.stack((red_csv, green_csv, blue_csv), axis=2)
        return RGB_image
    else:
        print("ERROR: There is a combination or verification error.")

# %% Task-4: Vizualization-----------------------------------------------------

# create a visualization for provided combined RGB_image data. To be used
# in-tandem with combine_RGB to verify data integrity and combine csv's.
def display_RGB_image(RGB_image):
    plt.imshow(RGB_image)
    plt.show()

# standalone test of display_RGB_image
# display_RGB_image(blue_csv)                  # Visualize a single color band

'''
Main function takes three input csv's for each RGB color band and
produces a single output RGB image.

Inputs:
    Input-1: Name of csv for red color band (str)    -> IE: "red.csv"
    Input-2: Name of csv for green color band (str)  -> IE: "green.csv"
    Input-3: Name of csv for blue color band (str)   -> IE: "blue.csv"
'''
def main(red, green, blue):
    RGB_image = combine_RGB(red, green, blue)
    display_RGB_image(RGB_image)
    return RGB_image

# %% Task-4b: Display Created Image--------------------------------------------

print("\nCheck Task: Combined RGB Image")
RGB_output = main("red.csv", "green.csv", "blue.csv")

# %%---------------------------------------------------------------------------
#
# END
#
