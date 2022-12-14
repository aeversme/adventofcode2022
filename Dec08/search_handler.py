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
    higher = True
    row = position[0]
    column = position[1]
    tree = trees[row][column]
    tree_to_compare = trees[row + direction[0]][column + direction[1]]
    if tree_to_compare >= tree:
        higher = False
    return higher


def is_visible(position, trees):
    visible = True
    row = position[0]
    column = position[1]
    directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]

    return visible
