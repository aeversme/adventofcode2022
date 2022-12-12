# Advent of Code 2022
# December 7th

from input_handler import convert_input
import tree_handler as th

with open('directorytree.txt') as file:
    dt_raw = file.readlines()

dt = convert_input(dt_raw)
print(dt)


def create_directory_tree(data):
    dir_list = th.populate_directories(data)
    for directory in dir_list:
        th.add_to_parent_size(directory)
    return dir_list


def get_small_dir_sum(data):
    dir_list = create_directory_tree(data)
    small_dir_sum = 0
    for directory in dir_list:
        if directory.size <= 100000:
            small_dir_sum += directory.size
    return small_dir_sum


small_sum = get_small_dir_sum(dt)
print(f'Sum of small directories = {small_sum}')
