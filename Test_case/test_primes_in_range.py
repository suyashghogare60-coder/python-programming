import sys
sys.path.append("code")
from primes_in_range import prime_range


def test_1_to_10():
    assert prime_range(1, 10) == [2, 3, 5, 7]


def test_10_to_20():
    assert prime_range(10, 20) == [11, 13, 17, 19]


def test_single_prime():
    assert prime_range(7, 7) == [7]


def test_no_prime():
    assert prime_range(8, 10) == []


def test_1_to_5():
    assert prime_range(1, 5) == [2, 3, 5]
print("All test cases passed.")