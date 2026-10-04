def prime_range(start, end):
    result = []

    for num in range(start, end + 1):
        if num > 1:
            flag = True

            for i in range(2, num):
                if num % i == 0:
                    flag = False
                    break

            if flag:
                result.append(num)

    return result


if __name__ == "__main__":
    start = int(input("Enter starting number: "))
    end = int(input("Enter ending number: "))

    print("Prime numbers:", prime_range(start, end))
