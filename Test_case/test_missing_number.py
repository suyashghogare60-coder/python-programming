import sys
sys.path.append("code")

from missing_number import find_missing_number

assert find_missing_number([1, 2, 3, 5]) == 4
assert find_missing_number([1, 2, 4, 5]) == 3
assert find_missing_number([1, 3, 4, 5]) == 2
assert find_missing_number([2, 3, 4, 5]) == 1
assert find_missing_number([1, 2, 3, 4, 6]) == 5

print("All test cases passed!")