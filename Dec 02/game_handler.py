code_guide = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors'
}

score_guide = {
    'rock': 1,
    'paper': 2,
    'scissors': 3,
    'lose': 0,
    'draw': 3,
    'win': 6
}


def count_games(games_list):
    """
    Takes a list of game outcomes, counts the number of each game outcome, i.e. 'A X' or 'C Z', and returns a dictionary
    :param games_list: list
    :return: dict
    """
    games_dict = {}
    for game in games_list:
        if game not in games_dict.keys():
            games_dict[game] = 1
        else:
            games_dict[game] += 1
    return games_dict


def determine_outcome(opponent_play, self_play):
    game_result = None
    if opponent_play == self_play:
        game_result = 'draw'
    else:
        if opponent_play == 'rock':
            if self_play == 'paper':
                game_result = 'win'
            elif self_play == 'scissors':
                game_result = 'lose'
        elif opponent_play == 'paper':
            if self_play == 'scissors':
                game_result = 'win'
            elif self_play == 'rock':
                game_result = 'lose'
        else:
            if self_play == 'rock':
                game_result = 'win'
            elif self_play == 'paper':
                game_result = 'lose'
    return game_result


def score_game(game, letter_dict, score_dict):
    """
    Takes a game (i.e. 'B Z'), determines the Rock, Paper, Scissors winner, and returns an integer score
    :param game: str
    :param letter_dict: dict
    :param score_dict: dict
    :return: int
    """
    opponent_play = game[0]
    self_play = game[2]
    game_result = determine_outcome(letter_dict[opponent_play], letter_dict[self_play])
    self_score = score_dict[game_result] + score_dict[letter_dict[self_play]]
    return self_score
