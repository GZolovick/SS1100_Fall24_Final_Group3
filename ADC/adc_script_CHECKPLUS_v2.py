# %% Version-2 Update Note-----------------------------------------------------

'''
Version 2 of adc_script_CHECKPLUS modifies the original version based off
ChatGPT 4o inputs on creating a callable change_orientation function rather
than adjusting the desired_orientation values manually with in-line code of v1.
'''

# %% Import Libraries and Scripts----------------------------------------------

import rotate_me
import calculate_rotation_v2 # Check-Plus Requirement

# %% Define Tolerance Check----------------------------------------------------

def tolerance_check(current_orientation, desired_orientation):
    if (abs(current_orientation[0] - desired_orientation[0]) <= 0.1 and
        abs(current_orientation[1] - desired_orientation[1]) <= 0.1 and
        abs(current_orientation[2] - desired_orientation[2]) <= 0.1):
        return True
    else:
        return False

# %% Define Change Orientation Command-----------------------------------------

'''
This function adjusts the satellites current orientation to a provided
desired orientation within a tolerance of 0.1 for each x-y-z axis value.

Input Variables:
    Input-1: location path of the current orientation file (str)
        -> str converts into tuple via calculate_rotation code
    Input-2: three-item tuple (x-y-z) values of desired orientation
'''

def change_orientation(current_state_file, desired_orientation):

    # define while-loop to run until rotate_me is within 0.1 tolerance
    while True:
    
        # run calculate_rotation to determine current orientation values
        current_orientation = calculate_rotation_v2.read_orientation_from_file(current_state_file)
        
        # break while-loop if current orientation is within 0.1 tolerance
        if tolerance_check(current_orientation, desired_orientation) == True:
            break
        
        # run calculate_rotation to determine required magnitude adjustments
        required_magnitude = calculate_rotation_v2.main(
                                 current_orientation, desired_orientation)
    
        # display required orientation adjustments
        print(f"\nRequired orientation change is: x {required_magnitude[0]}, y {required_magnitude[1]}, z {required_magnitude[2]}")
    
        # run rotate_me for each orientation change command
        rotate_me.main(required_magnitude)

# %% Test Cases

'''
Before running a new test case (IE, changing the desired_orientation values),
delete the existing current_state.txt file and re-run the rotate_me script.
'''

change_orientation("current_state.txt", (3,30,300))

# %%---------------------------------------------------------------------------
#
# END
#
