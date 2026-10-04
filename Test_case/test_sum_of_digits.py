import sys
sys.path.append("Code")

from sum_of_digits import sum_of_digits

assert sum_of_digits(12345) == 15
assert sum_of_digits(123) == 6
assert sum_of_digits(100) == 1
assert sum_of_digits(0) == 0
assert sum_of_digits(999) == 27

print("All test cases passed!")
