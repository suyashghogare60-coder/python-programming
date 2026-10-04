import sys
sys.path.append("code")
from fibonacci_series import fibonacci


def test_five_terms():
    assert fibonacci(5) == [0, 1, 1, 2, 3]


def test_three_terms():
    assert fibonacci(3) == [0, 1, 1]


def test_one_term():
    assert fibonacci(1) == [0]


def test_zero_terms():
    assert fibonacci(0) == []


def test_seven_terms():
    assert fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]
print("All test cases passed.")