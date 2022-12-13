# Advent of Code 2022
# December 2nd

from input_handler import convert_input
import game_handler as gh

with open('rps.txt') as file:
    rps_raw = file.readlines()

rps = convert_input(rps_raw)


def get_total_score(game_list, part_two=False):
    """
    Takes a list of RPS games and returns the score.
    :param game_list: list
    :param part_two: Boolean
    :return: int
    """
    total_score = 0
    for game in game_list:
        if part_two:
            total_score += gh.score_game(game, gh.code_guide, gh.score_guide, gh.self_shape, part_two=True)
        else:
            total_score += gh.score_game(game, gh.code_guide, gh.score_guide)
    return total_score


# Part one solution

rps_score = get_total_score(rps)
print(rps_score)

# Part two solution

rps_score_two = get_total_score(rps, part_two=True)
print(rps_score_two)
