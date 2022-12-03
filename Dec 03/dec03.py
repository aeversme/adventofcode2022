# Advent of Code 2022
# December 3rd

from input_handler import convert_input
import string_handler as sh

with open('rucksack.txt') as file:
    rucksack_raw = file.readlines()

rucksack_list = convert_input(rucksack_raw)
print(rucksack_list)


def calculate_priorities(rucksacks, part_two=False):
    """
    Takes a list of strings and returns a score.
    :param rucksacks: list
    :param part_two: Boolean
    :return: int
    """
    priority_total = 0
    if part_two:
        group_list = sh.group_strings(rucksacks)
        for group in group_list:
            common_letter = sh.find_common_letter(group_list=group, part_two=True)
            priority_total += sh.score_letter(common_letter)
    else:
        for rucksack in rucksacks:
            common_letter = sh.find_common_letter(string=rucksack)
            priority_total += sh.score_letter(common_letter)
    return priority_total


# Part one solution

total = calculate_priorities(rucksack_list)
print(total)

# Part two solution

group_total = calculate_priorities(rucksack_list, part_two=True)
print(group_total)
