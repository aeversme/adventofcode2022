# Advent of Code 2022
# December 4th

from input_handler import convert_input

with open('elfpairs_sample.txt') as file:
    pairs_raw = file.readlines()

pairs = convert_input(pairs_raw)
print(pairs)
