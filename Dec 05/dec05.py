# Advent of Code 2022
# December 5th

from input_handler import convert_input
import crate_handler as ch

with open('crates.txt') as file:
    crates_raw = file.readlines()

crates, procedures = convert_input(crates_raw)
crates_copy = crates.copy()


def find_top_crates(crate_list, procedure_list, part_two=False):
    """
    Takes a string list of 'crates' and a string list of 'procedures' and an optional Boolean, and returns a string \
    representing the top 'crate' in each stack.
    :param crate_list: list
    :param procedure_list: list
    :param part_two: Boolean
    :return: str
    """
    moved_crates = ch.restack_crates(crate_list, procedure_list, part_two)
    crates_string = ''
    for stack in moved_crates:
        crates_string += stack[-1]
    return crates_string


# Part one solution

top_crates = find_top_crates(crates, procedures)
print(top_crates)

# Part two solution

top_crates_9001 = find_top_crates(crates_copy, procedures, part_two=True)
print(top_crates_9001)
