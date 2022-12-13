from ..search_handler import is_edge
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
