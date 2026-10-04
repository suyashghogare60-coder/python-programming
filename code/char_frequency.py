def char_frequency(text):
    frequency = {}

    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    return frequency


if __name__ == "__main__":
    text = input("Enter a string: ")

    print("Character frequency:", char_frequency(text))
