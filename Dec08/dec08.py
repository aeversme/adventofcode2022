# Advent of Code 2022
# December 8th

from input_handler import convert_input
import search_handler as sh

with open('trees_sample.txt') as file:
    trees_raw = file.readlines()

trees = convert_input(trees_raw)
print(trees)


def count_visible_trees(data):
    count = 0
    for x in range(0, len(data) - 1):
        for y in range(0, len(data[0]) - 1):
            if sh.is_visible([x, y], data):
                count += 1
    return count


visible_count = count_visible_trees(trees)
print(visible_count)
