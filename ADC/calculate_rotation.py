# %% Script Purpose

'''
This script will calculate the x-y-z magnitude differences between
the current and desired orientatons and output a three-item tuple to be
sent to rotate_me for orientation adjustment commands.

Input Variables:
    Input-1: variable name of the text file for current orientation values
    Input-2: three-item tuple (x-y-z) values of desired orientation
'''

# %% Determine Current Orientation
def read_orientation_from_file(file_path):                     # based off provided rotate_me script
        with open(file_path, 'r') as file:
            line = file.readline().strip()
            orientation = tuple(map(float, line.split(','))) 
            return orientation
        
# %% Calculate X-Y-Z Magnitude Differences
def main(file_path, desired_orientation):
    
    # define current orientation values based on input text file
    current_orientation = read_orientation_from_file(file_path)
    
    # calculate difference between current and desired orientations
    magnitude_x = desired_orientation[0] - current_orientation[0]
    magnitude_y = desired_orientation[1] - current_orientation[1]
    magnitude_z = desired_orientation[2] - current_orientation[2]
    
    # return x-y-z magnitude differences
    magnitudes = (magnitude_x,magnitude_y,magnitude_z)
    return magnitudes

# %%
#
# END
#