import sys
sys.path.append("code")

from word_frequency import word_frequency

assert word_frequency("hello world hello") == {
    "hello": 2,
    "world": 1
}

assert word_frequency("python is easy python") == {
    "python": 2,
    "is": 1,
    "easy": 1
}

assert word_frequency("apple apple banana") == {
    "apple": 2,
    "banana": 1
}

assert word_frequency("Hello hello HELLO") == {
    "hello": 3
}

assert word_frequency("") == {}

print("All test cases passed!")