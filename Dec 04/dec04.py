# Advent of Code 2022
# December 4th

from input_handler import convert_input

with open('elfpairs.txt') as file:
    pairs_raw = file.readlines()

pairs = convert_input(pairs_raw)
# print(pairs)


def find_subsets(pairs_list):
    subset_total = 0
    for set_pair in pairs_list:
        if set_pair[0].issubset(set_pair[1]) or set_pair[0].issuperset(set_pair[1]):
            subset_total += 1
    return subset_total


# Part one solution

subsets = find_subsets(pairs)
print(subsets)
