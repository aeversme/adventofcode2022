letter_guide = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors'
}


def count_games(games_list):
    games_dict = {}
    for game in games_list:
        if game not in games_dict.keys():
            games_dict[game] = 1
        else:
            games_dict[game] += 1
    return games_dict
