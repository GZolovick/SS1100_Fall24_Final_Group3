# %% Import Libraries----------------------------------------------------------

import pandas as pd  # used to import raw RGB files
import numpy as np  # used to stack/combine RGB files
import matplotlib.pyplot as plt  # used for visualizations

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
        #True, print("Dimensions are equal")
        verification = True
        return (verification)


# %% Task-3: Combine RGB Bands-------------------------------------------------

# test if dimensions of inputs are equal, then combines into one RGB image
def combine_RGB(red, green, blue):
    verification = dimension_verification(red, green, blue)
    if  verification == True:
        #print("Dimensions are verified")
        RGB_image = np.stack((red, green, blue), axis=2).astype(np.uint8)
        return RGB_image
    else:
        print("There is a combination or verification error")

'''
When run, throws the following error:
    "self._normalize_image_array(A)"
    ** Verification function was not returning a true value, works now.
    ** Displays an image of Hermann Hall
'''

# %% Task-4: Vizualization-----------------------------------------------------

# create a visualization for provided combined RGB_image data. To be used
# in-tandem with combine_RGB to verify data integrity and combine csv's.
def display_RGB_image(RGB_image):
    plt.imshow(RGB_image)
    plt.show()

# standalone test of display_RGB_image
# display_RGB_image(blue_csv)                                           # Visualize a single color band
#display_RGB_image(combine_RGB(red_csv, green_csv, blue_csv))           # Result for the Check

# %% CheckPlus-1: Convert to Reflectance---------------------------------------
def radiance_to_reflectance(RGB_image, k, b):       # Where k is multiplicative and b is additive scaling factors
    reflectance = k * RGB_image + b
    return reflectance

# %% CheckPlus-2: Rescale Reflectance to 8-Bit---------------------------------
def rescale(converted_image):
    rescaled_image = 255 * converted_image
    rescaled_image = rescaled_image.astype(int)
    return rescaled_image

# %% CheckPlus-3: Save the output image to a file------------------------------
# Must save as a specific filename and in a specific folder

# %% Test Case for the Check Plus Portion
RGB_image = combine_RGB(red_csv, green_csv, blue_csv)
converted_image = radiance_to_reflectance(RGB_image,0.8,0.1)        # Should convert each pixel to the range [0,1]
''' Above line of code is not returning a viable image'''
#converted_image = radiance_to_reflectance(RGB_image,0.0039,0.0)          # Testing different k and b values
rescaled_image = rescale(converted_image)
display_RGB_image(rescaled_image)

# %%---------------------------------------------------------------------------
#
# END
#
