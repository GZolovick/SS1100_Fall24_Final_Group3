import random
import os
import sys

file_name = "current_state.txt" 

def apply_corrections(current_orientation, corrections):
    random_factor = random.uniform(0.95, 1.05)
    new_tuple = (
        current_orientation[0] + corrections[0] * random_factor,
        current_orientation[1] + corrections[1] * random_factor,
        current_orientation[2] + corrections[2] * random_factor
    )
    return new_tuple

def read_orientation_from_file(file_path):
    cwd = os.getcwd()
    full_file_path = os.path.join(cwd, file_path)
    if os.path.exists(full_file_path):
        with open(full_file_path, 'r') as file:
            line = file.readline().strip()
            orientation = tuple(map(float, line.split(',')))
    else:
        orientation = (random.randint(0, 360), random.randint(0, 360), random.randint(0, 360))
        write_orientation_to_file(full_file_path, orientation)
    return orientation

def write_orientation_to_file(file_path, orientation):
    cwd = os.getcwd()
    full_file_path = os.path.join(cwd, file_path)
    with open(full_file_path, 'w') as file:
        file.write(','.join(map(str, orientation)))

def main(input_tuple):
    starting_tuple = read_orientation_from_file(file_name)
    print(f"\nCurrent orientation is: x {starting_tuple[0]}, y {starting_tuple[1]}, z {starting_tuple[2]}")
    corrections = (input_tuple[0],input_tuple[1],input_tuple[2])
    result = apply_corrections(starting_tuple, corrections)
    write_orientation_to_file(file_name, result)
    print(f"\nNew orientation is: x {result[0]}, y {result[1]}, z {result[2]}")

if __name__ == "__main__":
    read_orientation_from_file(file_name)
