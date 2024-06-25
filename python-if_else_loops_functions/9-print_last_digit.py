#!/usr/bin/python3
def print_last_digit(number):
    last_digit = abs(number) % 10
    print(last_digit, end='')
    return last_digit

# Test the function
if __name__ == "__main__":
    print_last_digit(98)    # 8
    print_last_digit(0)     # 0
    r = print_last_digit(-1024)  # 4
    print(r)                # 4
