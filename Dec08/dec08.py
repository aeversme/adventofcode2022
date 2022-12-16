# Advent of Code 2022
# December 8th

from input_handler import convert_input
import search_handler as sh

with open('trees_sample.txt') as file:
    trees_raw = file.readlines()

trees = convert_input(trees_raw)
print(trees)


def count_visible_trees(data, part_two=False):
    count = 0
    largest_count = 0
    for x in range(0, len(data)):
        for y in range(0, len(data[0])):
            visible, view_count = sh.is_visible([x, y], data)
            if part_two:
                if visible:
                    if view_count > largest_count:
                        largest_count = view_count
            else:
                if visible:
                    count += 1
    return count, largest_count


# Part one solution

visible_count, _ = count_visible_trees(trees)
print(visible_count)

#  Part two solution

visible_count, visibility = count_visible_trees(trees, part_two=True)
print(visibility)
