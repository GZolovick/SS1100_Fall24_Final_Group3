# %% Import Libraries and Scripts

import rotate_me
import calculate_rotation # Check-Plus Requirement

# %% Define Maneuver Variables

# define current orientation file name
file_name = "current_state.txt"

# define desired orientation
desired_orientation = (3,30,300)

# %% Run Calculation and Rotation Scripts

# setup parameters to run both calculation and rotation scripts until required
# magnitiude adjustments are within 0.1 of each x-y-z desired_orientation value
magnitude_x = desired_orientation[0] - calculate_rotation.read_orientation_from_file(file_name)[0]
magnitude_y = desired_orientation[1] - calculate_rotation.read_orientation_from_file(file_name)[1]
magnitude_z = desired_orientation[2] - calculate_rotation.read_orientation_from_file(file_name)[2]

# print initial current_state values
starting_tuple = calculate_rotation.read_orientation_from_file(file_name)
print(f"\nCurrent orientation is: x {starting_tuple[0]}, y {starting_tuple[1]}, z {starting_tuple[2]}")

# define while loop to run until each x-y-z value is within 0.1 of desired_orientation value
while abs(magnitude_x) > 0.1 or abs(magnitude_y) > 0.1 or abs(magnitude_z) > 0.1:
    
    # run calculate_me for each orientation command
    required_magnitude = calculate_rotation.main(
                             file_name,
                             desired_orientation)
    
    # display required orientation adjustments
    print(f"\nThe required orientation change is: x {required_magnitude[0]}, y {required_magnitude[1]}, z {required_magnitude[2]}")
    
    # run rotate_me for each orientation change command
    rotate_me.main((required_magnitude[0],required_magnitude[1],required_magnitude[2]))
    
    if required_magnitude == (0,0,0):
        break

# %%
#
# END
#
