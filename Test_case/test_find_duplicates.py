import sys
sys.path.append("code")

from find_duplicates import find_duplicates

assert find_duplicates([1, 2, 2, 3, 4, 4]) == [2, 4]
assert find_duplicates([5, 5, 5, 5]) == [5]
assert find_duplicates([1, 2, 3, 4]) == []
assert find_duplicates([3, 1, 3, 2, 1]) == [3, 1]
assert find_duplicates([]) == []

print("All test cases passed!")