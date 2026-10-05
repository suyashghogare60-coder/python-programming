def find_common_elements(list1, list2):
    result = []

    for num in list1:
        if num in list2 and num not in result:
            result.append(num)

    return result


if __name__ == "__main__":
    list1 = list(map(int, input("Enter first list numbers separated by space: ").split()))
    list2 = list(map(int, input("Enter second list numbers separated by space: ").split()))

    print("Common elements:", find_common_elements(list1, list2))