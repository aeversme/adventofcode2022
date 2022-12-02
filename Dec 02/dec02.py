# Advent of Code 2022
# December 2nd

from input_handler import convert_input

with open('rps_sample.txt') as file:
    rps_raw = file.readlines()

rps = convert_input(rps_raw)


def count_games(games_list):
    games_dict = {}
    for game in games_list:
        if game not in games_dict.keys():
            games_dict[game] = 1
        else:
            games_dict[game] += 1
    return games_dict


counted_games = count_games(rps)
print(counted_games)
