# Advent of Code 2022
# December 2nd

from input_handler import convert_input
import game_handler as gh

with open('rps.txt') as file:
    rps_raw = file.readlines()

rps = convert_input(rps_raw)


def get_total_score(game_list):
    total_score = 0
    for game in game_list:
        total_score += gh.score_game(game, gh.code_guide, gh.score_guide)

    return total_score


# Part one solution

rps_score = get_total_score(rps)
print(rps_score)
