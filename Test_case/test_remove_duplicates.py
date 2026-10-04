import sys
sys.path.append("Code")

from remove_duplicates import remove_duplicates

assert remove_duplicates([1, 2, 2, 3, 3, 4]) == [1, 2, 3, 4]
assert remove_duplicates([1, 1, 1, 1]) == [1]
assert remove_duplicates([1, 2, 3]) == [1, 2, 3]
assert remove_duplicates([]) == []
assert remove_duplicates([5, 5, 6, 7, 6]) == [5, 6, 7]

print("All test cases passed!")
