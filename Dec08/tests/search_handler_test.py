from ..search_handler import is_edge, is_higher, is_visible
from ..input_handler import convert_input


def setup():
    with open('trees_sample.txt') as file:
        trees_raw = file.readlines()
    trees = convert_input(trees_raw)
    return trees


def test_is_edge():
    trees = setup()
    num1 = [1, 2]
    num2 = [3, 5]
    num3 = [-1, 2]
    num4 = [0, 4]
    num5 = [2, 4]

    assert is_edge(num1, trees) is not True
    assert is_edge(num2, trees) is None
    assert is_edge(num3, trees) is None
    assert is_edge(num4, trees)
    assert is_edge(num5, trees)


def test_is_higher():
    trees = setup()
    position1 = [3, 3]
    position2 = [2, 1]
    direction1 = [-1, 0]
    direction2 = [1, 0]
    direction3 = [0, -1]
    direction4 = [0, 1]

    assert is_higher(position1, direction1, trees)
    assert is_higher(position1, direction2, trees) is not True
    assert is_higher(position1, direction3, trees) is not True
    assert is_higher(position1, direction4, trees) is not True
    assert is_higher(position2, direction1, trees) is not True
    assert is_higher(position2, direction2, trees)
    assert is_higher(position2, direction3, trees) is not True
    assert is_higher(position2, direction4, trees)


def test_is_visible():
    trees = setup()
    position1 = [1, 1]
    position2 = [2, 1]
    position3 = [2, 2]
    position4 = [3, 1]
    position5 = [3, 3]

    assert is_visible(position1, trees)
    assert is_visible(position2, trees)
    assert is_visible(position3, trees) is not True
    assert is_visible(position4, trees) is not True
    assert is_visible(position5, trees) is not True
