def is_palindrome(n):
    if n < 0:
        return False

    original = n
    reversed_number = 0

    while n > 0:
        digit = n % 10
        reversed_number = reversed_number * 10 + digit
        n = n // 10

    return original == reversed_number


if __name__ == "__main__":
    n = int(input("Enter a number: "))

    if is_palindrome(n):
        print("Palindrome number")
    else:
        print("Not a palindrome number")
