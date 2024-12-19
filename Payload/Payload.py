# %% Import Libraries----------------------------------------------------------

import pandas as pd                # used to import raw RGB files
import numpy as np                 # used to stack/combine RGB files
import matplotlib.pyplot as plt    # used for vizualizations

# %% Task-1: Load Raw RGB Input Files------------------------------------------

red_csv = pd.read_csv("red.csv").values
green_csv = pd.read_csv("green.csv").values
blue_csv = pd.read_csv("blue.csv").values

# %% Task-2: Verify RGB Band Dimensions----------------------------------------

# verifies equal dimensions for each input csv
def dimension_verification(red, green, blue):
    if red.shape != blue.shape or red.shape != green.shape:
        False, print("ERROR: The provided RGB files do not have the same size.")
    else:
        True
        
# %% Task-3: Combine RGB Bands-------------------------------------------------

# test if dimensions of inputs are equal, then combines into one RGB image
def combine_RGB(red, green, blue):
    verification = dimension_verification(red, green, blue)
    if verification == True:
        RGB_image = np.stack((red, green, blue), axis=2).astype(np.uint8)
        return RGB_image
    else:
         print("There is a combination or verification error")

'''
When run, throws the following error:
    "self._normalize_image_array(A)"
    ** Verification function was not returning a true value, works now.
    ** Displays a color distorted image of Hermann Hall
'''

# %% Task-4: Vizualization-----------------------------------------------------

# create a visualization for provided combined RGB_image data. To be used
# in-tandem with combine_RGB to verify data integrity and combine csv's.
def display_RGB_image(RGB_image):
    plt.imshow(RGB_image)
    plt.show()

# standalone test of display_RGB_image
display_RGB_image(combine_RGB(red_csv, green_csv, blue_csv))

# %% CheckPlus-1: Convert to Reflectance---------------------------------------


# %% CheckPlus-2: Rescale Reflactance to 8-Bit---------------------------------


# %%---------------------------------------------------------------------------
#
# END
#
