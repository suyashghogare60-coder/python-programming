import sys
sys.path.append("Code")

from vowels_consonants import count_vowels_consonants

assert count_vowels_consonants("hello") == (2, 3)
assert count_vowels_consonants("python") == (1, 5)
assert count_vowels_consonants("aeiou") == (5, 0)
assert count_vowels_consonants("xyz") == (0, 3)
assert count_vowels_consonants("Hello World") == (3, 7)

print("All test cases passed!")
