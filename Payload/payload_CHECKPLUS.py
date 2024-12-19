'''
CheckPlus script created with StackOverflow tutorials on saving images to 
specific folders and through ChatGPT 4o assistance for error handling.

Prompt: "This line of code produced the following error. Help me troubleshoot:
"TypeError: unsupported operand type(s) for *: 'NoneType' and 'int' " ".

From the prompt, an error was located in how the image file was being created
within the original payload.py script. The payload.main function was returning
the image alone, and not the associated data. This led to adjustments in both
payload.py (changing the main function to return the RGB image data along with
the produced image) and within payload_CHECKPLUS.py for how the functions
radiance_to_reflection and rescale handled the data produced by payload.main().
'''

# %% Import Libraries----------------------------------------------------------

import numpy as np        # used to stack/combine RGB files
import payload            # used to call RGB output and payload.py functions
from PIL import Image     # used to save image files
import os                 # used to save image files

# %% Call RGB Output from Payload.py

RGB_output = payload.main("red.csv", "green.csv", "blue.csv")

# standalone test of RGB_output call:
#print(RGB_output)
#print(type(RGB_output))   # expecting valid NumPy array
#print(RGB_output.dtype)   # expecting int64
#print(RGB_output.shape)   # expecting 3-digit shape

# %% CheckPlus-1: Convert Radiance to Reflectance------------------------------

'''
This function takes three-inputs and converts the input reflectance into
radiance through the formula: image * k + b.

Inputs:
    Input-1: RGB image file to be converted (var)
    Input-2: k, the multiplicative scaling factor (int)
    Input-3: b, the additive scaling factor (int)
'''
def radiance_to_reflectance(RGB_image, k, b):
    if RGB_image is None:
        raise ValueError("ERROR: Input image is None. Provide a valid image.")
    
    else:
        # normalize image to [0, 1] range
        normalized_image = RGB_image / 255.0

        # calculate reflectance
        reflectance_image = k * normalized_image + b

        return reflectance_image

# standalone test of radiance_to_reflectance:
#reflectance_image = radiance_to_reflectance(RGB_output, 0.8, 0.1)
#print(type(reflectance_image))   # expecting valid NumPy array
#print(reflectance_image.dtype)   # expecting float64
#print(reflectance_image.min())   # expecting min-max values between [0,1]
#print(reflectance_image.max())   #                  "

# %% CheckPlus-2: Rescale Reflectance to 8-Bit---------------------------------

'''
This function take a single reflectance RGB image and rescales it into
8-bit digitial number format to optimize size and decrease tranmission times.
Designed to take its input as the output from function radiance_to_reflectance.

Input: RGB image converted from radiance to reflectance (var)
'''
def rescale(converted_image):
    
    # adjust floating point values
    rescaled_image = (converted_image * 255)
    
    # convert to 8-bit integers
    rescaled_image = rescaled_image.astype(np.uint8)
    
    return rescaled_image

# standalone test of rescale:
#rescale_image = rescale(radiance_to_reflectance(RGB_output, 0.8, 0.1))
#print(type(rescale_image))   # expecting valid NumPy array
#print(rescale_image.dtype)   # expecting uint8
#print(rescale_image.shape)   # expecting 3-digit shape

# %% CheckPlus-3: Save the output image to a file------------------------------

def save_image(image, file_name, folder_location):
    
    try:
        # defines the full file path to save the image
        file_path = os.path.join(folder_location, file_name)
        
        # defines the image for PIL to save
        image_pil = Image.fromarray(image)
        
        # saves image with success message
        image_pil.save(file_path)
        print("Image saved successfully to:", file_path)
    
    # returns error message if file not saved
    except Exception as e:
        print("ERROR: Failed to save the requested image.", e)

# %% CheckPlus: Test and Evaluation--------------------------------------------

'''
Main function takes four-inputs and converts the input reflectance into
radiance through the formula: image * k + b.

Inputs:
    Input-1: RGB image file to be converted (var) -> IE: payload.main output
    Input-2: k, the multiplicative scaling factor (int)
    Input-3: b, the additive scaling factor (int)
    Input-4: file path to save the RGB_converted.jpeg image
'''
def main(RGB_image, k, b, file_path):
    
    # convert input RGB image
    reflectance_image = radiance_to_reflectance(RGB_image, k, b)
    # rescale reflectance image
    rescaled_image = rescale(reflectance_image)
    
    # save image file
    print("\nCheckPlus Task: Saving converted RGB image")
    save_image(rescaled_image, "RGB_converted_CHECKPLUS.png", file_path)
    
    return rescaled_image

# CheckPlus evaluation
RGB_converted = main(RGB_output, 0.8, 0.1,
                     r"C:\Users\Jake\OneDrive - Naval Postgraduate School\0) Coursework\SS1100\Final Project\Payload")
#print(type(RGB_converted))   # expecting valid NumPy array
#print(RGB_converted.dtype)   # expecting uint8
#print(RGB_converted.shape)   # expecting 3-digit shape

# %%---------------------------------------------------------------------------
#
# END
#
