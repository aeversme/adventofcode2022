# Advent of Code 2022
# December 8th

from input_handler import convert_input
import search_handler as sh

with open('trees_sample.txt') as file:
    trees_raw = file.readlines()

trees = convert_input(trees_raw)
print(trees)


