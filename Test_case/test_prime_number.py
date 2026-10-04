import sys
sys.path.append("code")
from prime_number import prime


def test_prime_7():
    assert prime(7) is True


def test_prime_13():
    assert prime(13) is True


def test_not_prime():
    assert prime(10) is False


def test_zero():
    assert prime(0) is False


def test_one():
    assert prime(1) is False
print("All test cases passed.")