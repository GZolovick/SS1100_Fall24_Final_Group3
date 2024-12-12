#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 13:32:15 2024

@author: sheadonnelly
"""
import numpy
import math
#Heat_energy = Q #joules
#mass = m #kilograms
#specific_heat_capacity = c #J/Kg*C
#Change_in_Temperature = delta_T #degC

#Q = m*c*delta_t

# Step 1: Floats
def temp_control(current_temp: float, target_temp: float):                     #Adjusts current_temp vlaue until it equals the target_temp value

    while abs(target_temp - current_temp) > 0.01:                              #Runs while loop until difference of target_temp and current_tmep is less than 0.01
    
# Step 2: 
        delta_T = target_temp - current_temp                                   #Calculates the difference b/w target_temp and current_temp 
    
# Step 3: 
        adjustment = 0.25 * delta_T                                            #Calculate current temp adjustment by no more than 25%
    
# Step 4:
       
        print(f"Adjust temperature by: {adjustment:.2f} degrees")              #Print how much temp needs to be adjusted by
        
        current_temp += adjustment                                             #updates current_temp for each loop
        
        print(f"The current temperature is now: {current_temp:.2f} degrees")   #Print what the new current temp is
        
#Step 5: Return as float for new current temp
    return current_temp                                                        #returns loop until current_temp is equal to target temp
    
#Example 1
if __name__ == "__main__":
    current_temp = 35.0
    target_temp = 20.0
    new_temp = temp_control(current_temp, target_temp)
    print(f"New sensor temperature is: {new_temp:.2f} degrees")                #Prints what the sensor temp is
    
    