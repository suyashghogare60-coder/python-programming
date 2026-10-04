def is_palindrome(text):
    return text == text[::-1]


if __name__ == "__main__":
    text = input("Enter a string: ")

    if is_palindrome(text):
        print("Palindrome string")
    else:
        print("Not a palindrome string")
