def split_string(string):
    """
    Takes a string and returns two strings.
    :param string: str
    :return: str
    """
    string_length = len(string)
    first_half = string[:string_length // 2]
    second_half = string[string_length // 2:]
    return first_half, second_half


def group_strings(string_list):
    """
    Takes a list of strings and returns a 2D list of strings, grouped into threes.
    :param string_list: list
    :return: list
    """
    string_groups = []
    group = []
    index = 0
    for i in range(len(string_list)):
        group.append(string_list[i])
        index += 1
        if index == 3:
            string_groups.append(group)
            group = []
            index = 0
    return string_groups


def find_common_letter(string=None, group_list=None, part_two=False):
    """
    Takes a string or list of strings, and returns the common letter between two halves of the string or all strings in
    the list.
    :param string: str
    :param group_list: list
    :param part_two: Boolean
    :return: str
    """
    if part_two:
        for letter in group_list[0]:
            if letter in group_list[1] and letter in group_list[2]:
                return letter
    else:
        first_half, second_half = split_string(string)
        for letter in first_half:
            if letter in second_half:
                return letter
    return None


def score_letter(letter):
    """
    Takes a single string character and returns an integer score.
    :param letter: str
    :return: int
    """
    if letter.isupper():
        # score between 27-52
        score = ord(letter) - 38
    else:
        # score between 1-26
        score = ord(letter) - 96
    return score
