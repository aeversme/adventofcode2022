# Advent of Code 2022
# December 7th

from input_handler import convert_input

with open('directorytree_sample.txt') as file:
    dt_raw = file.readlines()

dt = convert_input(dt_raw)
print(dt)
