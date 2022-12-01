# Advent of Code 2022
# December 1, part 1

import input_handler as ih

with open('calories.txt') as cal:
    calories_raw = cal.readlines()

calories_list = ih.convert_input(calories_raw)

# print(calories_raw)
# print(calories_list)
# print(calories_list[3] == '')


def sum_calories(calorie_list):
    new_elf_index = 0
    calorie_sum = 0
    elf_calorie_list = []
    while new_elf_index <= len(calorie_list) + 1:
        if new_elf_index == len(calorie_list):
            break
        for i in range(new_elf_index, len(calorie_list)):
            if calorie_list[i] != '':
                new_elf_index += 1
                calorie_sum += calorie_list[i]
            else:
                new_elf_index += 1
                elf_calorie_list.append(calorie_sum)
                calorie_sum = 0
    return elf_calorie_list


elf_calories = sum_calories(calories_list)
# print(elf_calories)
print(max(elf_calories))
