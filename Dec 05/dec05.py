# Advent of Code 2022
# December 5th

from input_handler import convert_input

with open('crates_sample.txt') as file:
    crates_raw = file.readlines()

crates = convert_input(crates_raw)
print(crates)
