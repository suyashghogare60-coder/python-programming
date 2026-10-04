import sys
sys.path.append("Code")

from palindrome_string import is_palindrome

assert is_palindrome("madam") == True
assert is_palindrome("racecar") == True
assert is_palindrome("hello") == False
assert is_palindrome("level") == True
assert is_palindrome("python") == False

print("All test cases passed!")
