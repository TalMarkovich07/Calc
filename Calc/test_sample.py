import pytest
from main import run_calculator as calculate

def test_basic_operators():
    assert calculate("2 + 3 * 4") == 14
    assert calculate("10 / 2 - 1") == 4
    assert calculate("2 ^ (3 ^ 2)") == 512
    assert calculate("4 @ 2") == 3
    assert calculate("5 & 10") == 5
    assert calculate("5 $ 2") == 5
    assert calculate("10 % 3") == 1

def test_hashtag_operator():
    assert calculate("123#") == 6
    assert calculate("2.3#") == 5
    assert calculate("123##") == 6

def test_unary_minus():
    assert calculate("-1 + 7") == 6
    assert calculate("-2 ^ 4") == -16
    assert calculate("2 - -3") == 5
    assert calculate("3 + ~-3") == 6
    assert calculate("-3!") == -6

def test_complex_expressions():
    assert calculate("(2 + 3 * (4 ^ 2)) / 10") == 5
    assert calculate("((10 $ 20) @ (30 & 50)) + 2!") == 27
    assert calculate("100 / (2 ^ 2) * 3 + 123#") == 81
