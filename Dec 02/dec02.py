# Advent of Code 2022
# December 2nd

from input_handler import convert_input
import game_handler as gh

with open('rps_sample.txt') as file:
    rps_raw = file.readlines()

rps = convert_input(rps_raw)

counted_games = gh.count_games(rps)
print(counted_games)

score = gh.score_game(rps[0], gh.letter_guide, gh.score_guide)
print(score)
