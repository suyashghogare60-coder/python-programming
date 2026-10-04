import sys
sys.path.append("Code")

from reverse_string import reverse_string

assert reverse_string("hello") == "olleh"
assert reverse_string("python") == "nohtyp"
assert reverse_string("abc") == "cba"
assert reverse_string("") == ""
assert reverse_string("12345") == "54321"

print("All test cases passed!")
