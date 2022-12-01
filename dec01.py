# Advent of Code 2022
# December 1, part 1

import input_handler as ih

with open('calories_sample.txt') as cal:
    calories_raw = cal.readlines()

calories_list = ih.convert_input(calories_raw)

print(calories_raw)
print(calories_list)
print(calories_list[3] == '')
