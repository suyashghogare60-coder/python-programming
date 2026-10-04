import sys
sys.path.append("code")
from reverse_number import reverse_number


def test_reverse_123():
    assert reverse_number(123) == 321


def test_reverse_12345():
    assert reverse_number(12345) == 54321


def test_single_digit():
    assert reverse_number(7) == 7


def test_zero():
    assert reverse_number(0) == 0


def test_ending_zero():
    assert reverse_number(1200) == 21
print("All test cases passed.")