# Advent of Code 2022
# December 6th

from input_handler import convert_input

with open('signal.txt') as file:
    signal_raw = file.readlines()

signal = convert_input(signal_raw)
print(signal)


def is_unique_marker(string):
    """
    Takes a string, and returns a Boolean based on if all characters in the string are unique.
    :param string: str
    :return: Boolean
    """
    all_unique = True
    for char in string:
        if string.count(char) > 1:
            all_unique = False
    return all_unique


def find_marker(signal_string, part_two=False):
    """
    Takes a string and an optional Boolean, and returns the integer value for the last character in the marker.
    :param signal_string: str
    :param part_two: Boolean
    :return: int
    """
    marker_length = 4
    if part_two:
        marker_length = 14
    index = marker_length
    for _ in range(len(signal_string) - marker_length):
        marker = signal_string[index - marker_length:index]
        if is_unique_marker(marker):
            break
        index += 1
    return index


# Part one solution

marker_start = find_marker(signal[0])
print(marker_start)

# Part two solution

message_start = find_marker(signal[0], part_two=True)
print(message_start)
