import unittest
import EightQueen


def test_one_queen():
    assert EightQueen.get_solution(1) == 1

def test_two_queen():
    assert EightQueen.get_solution(2) == 0

def test_three_queen():
    assert EightQueen.get_solution(3) == 0

def test_four_queen():
    assert EightQueen.get_solution(4) == 2

def test_five_queen():
    assert EightQueen.get_solution(5) == 10

def test_six_queen():
    assert EightQueen.get_solution(6) == 4

def test_seven_queen():
    result = EightQueen.get_solution(7)
    print(result)
    assert result == 40

def test_eight_queen():
    result = EightQueen.get_solution(8)
    print(result)
    assert result == 92

     