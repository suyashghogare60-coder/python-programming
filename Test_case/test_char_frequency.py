import sys
sys.path.append("Code")

from char_frequency import char_frequency

assert char_frequency("hello") == {
    "h": 1,
    "e": 1,
    "l": 2,
    "o": 1
}

assert char_frequency("aaa") == {
    "a": 3
}

assert char_frequency("abc") == {
    "a": 1,
    "b": 1,
    "c": 1
}

assert char_frequency("") == {}

assert char_frequency("aabbc") == {
    "a": 2,
    "b": 2,
    "c": 1
}

print("All test cases passed!")
