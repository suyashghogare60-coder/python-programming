def sum_of_digits(n):
    n = abs(n)
    total = 0

    while n > 0:
        digit = n % 10
        total = total + digit
        n = n // 10

    return total


if __name__ == "__main__":
    n = int(input("Enter a number: "))

    print("Sum of digits:", sum_of_digits(n))
