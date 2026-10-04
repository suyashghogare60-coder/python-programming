import sys
sys.path.append("code")
from factorial import factorial


def test_factorial_5():
    assert factorial(5) == 120


def test_factorial_4():
    assert factorial(4) == 24


def test_factorial_3():
    assert factorial(3) == 6


def test_factorial_1():
    assert factorial(1) == 1


def test_factorial_0():
    assert factorial(0) == 1
print("All test cases passed.")