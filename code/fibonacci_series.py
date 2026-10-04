def fibonacci(n):
    a = 0
    b = 1
    result = []

    for i in range(n):
        result.append(a)
        c = a + b
        a = b
        b = c

    return result


if __name__ == "__main__":
    n = int(input("Enter number of terms: "))

    print("Fibonacci series:", fibonacci(n))
