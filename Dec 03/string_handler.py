def split_string(string):
    string_length = len(string)
    first_half = string[:string_length // 2]
    second_half = string[string_length // 2:]
    return first_half, second_half


def find_common_letter(string):
    first_half, second_half = split_string(string)
    for letter in first_half:
        if letter in second_half:
            return letter
    return None


def score_letter(letter):
    if letter.isupper():
        score = ord(letter) - 38
    else:
        score = ord(letter) - 96
    return score
