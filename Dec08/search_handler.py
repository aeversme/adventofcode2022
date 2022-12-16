def is_edge(position, trees):
    """

    :param position:
    :param trees:
    :return:
    """
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


def is_higher(position, direction, trees, position_index=None):
    """
    Checks a given position's value against the value of an adjacent position in the grid of 'trees'. Returns True if
    the given position is higher (greater) than the adjacent position; otherwise, returns False.
    :param position_index:
    :param position:
    :param direction:
    :param trees:
    :return:
    """
    higher = True
    row = position[0]
    column = position[1]
    tree = trees[row][column]
    if position_index is not None:
        tree = trees[row - (direction[0] * position_index)][column - (direction[1] * position_index)]
    if is_edge(position, trees):
        higher = True
    else:
        tree_to_compare = trees[row + direction[0]][column + direction[1]]
        if tree_to_compare >= tree:
            higher = False
    return higher


def is_visible_in_one_direction(position, direction, trees, position_index=0):
    """

    :param position:
    :param direction:
    :param trees:
    :param position_index:
    :return:
    """
    row = position[0]
    column = position[1]
    position_index = position_index
    position_to_check = position
    if is_edge(position_to_check, trees):
        visible = True
    elif is_higher(position_to_check, direction, trees, position_index):
        position_index += 1
        position_to_check = [row + direction[0], column + direction[1]]
        visible, position_index = is_visible_in_one_direction(position_to_check, direction, trees, position_index)
    else:
        visible = False
    return visible, position_index


def is_visible(position, trees):
    """

    :param position:
    :param trees:
    :return:
    """
    visible = True
    directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    directions_visible = []
    view_count = 0
    if is_edge(position, trees):
        return True, view_count
    for direction in directions:
        direction_visible, direction_count = is_visible_in_one_direction(position, direction, trees)
        directions_visible.append(direction_visible)
        if view_count == 0:
            view_count += direction_count
        else:
            view_count *= direction_count
    if True not in directions_visible:
        visible = False
    return visible, view_count
