import sys
sys.path.append("code")

from common_elements import find_common_elements

assert find_common_elements([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]
assert find_common_elements([1, 2, 3], [4, 5, 6]) == []
assert find_common_elements([1, 2, 2, 3], [2, 3, 4]) == [2, 3]
assert find_common_elements([5, 6, 7], [5, 6, 7]) == [5, 6, 7]
assert find_common_elements([], [1, 2, 3]) == []

print("All test cases passed!")