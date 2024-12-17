# %% Import Libraries and Scripts

import rotate_me
import calculate_rotation # Check-Plus Requirement

# %% Define Maneuver Variables

# define current orientation file name
file_name = "current_state.txt"

# define desired orientation
desired_orientation = (3,30,300)

# %% Run Calculation Script

required_magnitude = calculate_rotation.main(
                         file_name,
                         desired_orientation)

# %% Run Rotation Script

rotate_me.main((required_magnitude[0],required_magnitude[1],required_magnitude[2]))

# %%
#
# END
#