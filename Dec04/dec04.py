# Advent of Code 2022
# December 4th

from input_handler import convert_input

with open('elfpairs.txt') as file:
    pairs_raw = file.readlines()

pairs = convert_input(pairs_raw)
# print(pairs)


def count_subsets(pairs_list):
    subset_total = 0
    for set_pair in pairs_list:
        if set_pair[0].issubset(set_pair[1]) or set_pair[0].issuperset(set_pair[1]):
            subset_total += 1
    return subset_total


def count_intersections(pairs_list):
    intersections = 0
    for set_pair in pairs_list:
        if not set_pair[0].isdisjoint(set_pair[1]):
            intersections += 1
    return intersections


# Part one solution

subsets = count_subsets(pairs)
print(subsets)

# Part two solution

overlaps = count_intersections(pairs)
print(overlaps)
