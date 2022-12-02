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

self_shape = {
    'rock': 'X',
    'paper': 'Y',
    'scissors': 'Z'
}


def determine_outcome(opponent_play, self_play):
    """
    Takes two strings representing RPS plays and returns a string representing the outcome
    :param opponent_play: str
    :param self_play: str
    :return: str
    """
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


def determine_shape(game, code_dict, shape_dict):
    """
    Takes a game (i.e. 'B Z'), determines the shape needed for the desired outcome, and returns the shape and the
    desired outcome
    :param game: str
    :param code_dict: dict
    :param shape_dict: dict
    :return: str
    """
    desired_outcome = {
        'X': 'lose',
        'Y': 'draw',
        'Z': 'win'
    }
    opponent_play = game[0]
    outcome = desired_outcome[game[2]]
    if outcome == 'draw':
        self_play = code_dict[opponent_play]
    else:
        if code_dict[opponent_play] == 'rock':
            self_play = 'paper'
            if outcome == 'lose':
                self_play = 'scissors'
        elif code_dict[opponent_play] == 'paper':
            self_play = 'scissors'
            if outcome == 'lose':
                self_play = 'rock'
        else:
            self_play = 'rock'
            if outcome == 'lose':
                self_play = 'paper'
    return outcome, shape_dict[self_play]


def score_game(game, code_dict, score_dict, shape_dict=None, part_two=False):
    """
    Takes a game (i.e. 'B Z'), determines the Rock, Paper, Scissors winner, and returns an integer score
    :param shape_dict: dict
    :param part_two: Boolean
    :param game: str
    :param code_dict: dict
    :param score_dict: dict
    :return: int
    """
    opponent_play = game[0]
    self_play = game[2]
    game_result = determine_outcome(code_dict[opponent_play], code_dict[self_play])
    if part_two:
        game_result, self_play = determine_shape(game, code_dict, shape_dict)
    self_score = score_dict[game_result] + score_dict[code_dict[self_play]]
    return self_score
