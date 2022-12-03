# Advent of Code 2022
# December 3rd

from input_handler import convert_input
import string_handler as sh

with open('rucksack.txt') as file:
    rucksack_raw = file.readlines()

rucksack_list = convert_input(rucksack_raw)
print(rucksack_list)


def calculate_priorities(rucksacks):
    priority_total = 0
    for rucksack in rucksacks:
        common_letter = sh.find_common_letter(rucksack)
        priority_total += sh.score_letter(common_letter)
    return priority_total


# Part one solution

total = calculate_priorities(rucksack_list)
print(total)
