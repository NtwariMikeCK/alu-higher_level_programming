#!/usr/bin/python3


def islower(c):
    if len(c) != 1:
        raise ValueError("Input must be a single character.")
    return ord(c) >= 97 and ord(c) <= 122


def main():
    test_cases = ['a', 'H', 'A', '3', 'g']
    for c in test_cases:
        result = "lower" if islower(c) else "upper"
        print("{} is {}".format(c, result))


if __name__ == "__main__":
    main()
