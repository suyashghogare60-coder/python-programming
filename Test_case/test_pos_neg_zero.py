import sys
sys.path.append("code")
from pos_neg_zero import check_number


def test_positive():
    assert check_number(10) == "Positive"


def test_negative():
    assert check_number(-10) == "Negative"


def test_zero():
    assert check_number(0) == "Zero"


def test_large_positive():
    assert check_number(1000) == "Positive"


def test_large_negative():
    assert check_number(-1000) == "Negative"
print("All test cases passed.")