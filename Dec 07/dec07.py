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


# Part one solution


def get_small_dir_sum(data):
    dir_list = create_directory_tree(data)
    small_dir_sum = 0
    for directory in dir_list:
        if directory.size <= 100000:
            small_dir_sum += directory.size
    return dir_list, small_dir_sum


dirs, small_sum = get_small_dir_sum(dt)
print(f'Sum of small directories = {small_sum}')


# Part two solution


def find_dir_to_delete(data):
    directories = create_directory_tree(data)
    total_size = directories[0].size
    print(f'Size of root = {total_size}')
    free_space = 70000000 - total_size
    amount_to_delete = 30000000 - free_space
    print(f'Amount to be deleted = {amount_to_delete}')
    eligible_dirs = []
    for d in directories:
        if d.size > amount_to_delete:
            eligible_dirs.append(d)
    print(f'Eligible directories = {len(eligible_dirs)}')
    smallest_size = total_size
    for e in eligible_dirs:
        if e.size < smallest_size:
            smallest_size = e.size
    return smallest_size


size = find_dir_to_delete(dt)
print(f'Directory size to delete = {size}')
