# %% Script Purpose------------------------------------------------------------

'''
This script will calculate the x-y-z magnitude differences between
the current and desired orientatons and output a three-item tuple to be
sent to rotate_me for orientation adjustment commands.

Inputs:
    Input-1: Current Orientation (tuple)
        -> called and converted to tuple inside the change_orientation
           function of main adc_script_CHECKPLUS_v2 code
    Input-2: Desired Orientation (tuple)
        -> provided via change_orientation function inputs
'''

# %% Determine Current Orientation---------------------------------------------
def read_orientation_from_file(file_path):                                      # based off provided rotate_me script
        with open(file_path, 'r') as file:
            line = file.readline().strip()
            orientation = tuple(map(float, line.split(','))) 
            return orientation

# %% Calculate X-Y-Z Magnitude Differences-------------------------------------
def main(current_orientation, desired_orientation):

    # calculate difference between current and desired orientations
    magnitude_x = desired_orientation[0] - current_orientation[0]
    magnitude_y = desired_orientation[1] - current_orientation[1]
    magnitude_z = desired_orientation[2] - current_orientation[2]

    # return x-y-z magnitude differences
    magnitudes = (magnitude_x, magnitude_y, magnitude_z)
    return magnitudes

# %%---------------------------------------------------------------------------
#
# END
#