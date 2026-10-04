import sys
sys.path.append("Code")

from second_largest import second_largest

assert second_largest([10, 20, 30]) == 20
assert second_largest([50, 10, 30, 20]) == 30
assert second_largest([5, 5, 3, 2]) == 3
assert second_largest([-10, -5, -20]) == -10
assert second_largest([1, 2, 3, 4, 5]) == 4

print("All test cases passed!")
