def factorial(num):
    fact = 1

    for i in range(1, num + 1):
        fact = fact * i

    return fact


if __name__ == "__main__":
    num = int(input("Enter a number: "))

    if num < 0:
        print("factorial is not possible")
    else:
        print("factorial is:",factorial(num))

