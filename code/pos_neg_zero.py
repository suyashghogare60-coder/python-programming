def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"


if __name__ == "__main__":
    num = int(input("Enter a number: "))

    print("Number is:", check_number(num))
