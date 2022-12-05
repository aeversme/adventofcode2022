# Advent of Code 2022
# December 5th

from input_handler import convert_input
import crate_handler as ch

with open('crates.txt') as file:
    crates_raw = file.readlines()

crates, procedures = convert_input(crates_raw)


def find_top_crates(crate_list, procedure_list):
    moved_crates = ch.restack_crates(crate_list, procedure_list)
    crates_string = ''
    for stack in moved_crates:
        crates_string += stack[-1]
    return crates_string


# Part one solution

top_crates = find_top_crates(crates, procedures)
print(top_crates)
