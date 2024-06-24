#!/usr/bin/python3


def uppercase(str):
    result = ""
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            result += chr(ord(char) - 32)
        else:
            result += char
    print("{}".format(result))


if __name__ == "__main__":
    uppercase("best")
    uppercase("Best School 98 Battery street")
