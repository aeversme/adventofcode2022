def is_edge(position, trees):
    edge = True
    horiz_length = len(trees[0])
    vert_length = len(trees)
    row = position[0]
    column = position[1]
    if row < 0 or row > vert_length - 1 or column < 0 or column > horiz_length - 1:
        print(f'Position {position} out of range.')
        return None
    elif 0 < row <= vert_length - 2 and 0 < column <= horiz_length - 2:
        edge = False
    return edge


def is_higher(position, direction, trees):
    """
    Checks a given position's value against the value of an adjacent position in the grid of 'trees'. Returns True if
    the given position is higher (greater) than the adjacent position; otherwise, returns False.
    :param position:
    :param direction:
    :param trees:
    :return:
    """
    higher = True
    row = position[0]
    column = position[1]
    tree = trees[row][column]
    tree_to_compare = trees[row + direction[0]][column + direction[1]]
    if tree_to_compare >= tree:
        higher = False
    return higher


def is_visible_in_one_direction(position, direction, trees):
    visible = True
    row = position[0]
    column = position[1]
    position_to_check = position
    if is_edge(position_to_check, trees):
        visible = is_higher(position_to_check, direction, trees)
    elif is_higher(position_to_check, direction, trees):
        position_to_check = [row + direction[0], column + direction[1]]
        visible = is_higher(position_to_check, direction, trees)
    return visible


def is_visible(position, trees):
    visible = True
    directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    directions_visible = []
    if is_edge(position, trees):
        return True
    for direction in directions:
        direction_visible = is_visible_in_one_direction(position, direction, trees)
        directions_visible.append(direction_visible)
    if True not in directions_visible:
        visible = False
    return visible
