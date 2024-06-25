#!/usr/bin/python3
def pow(a, b):
    return a ** b

# Test the function
if __name__ == "__main__":
    print(pow(2, 2))         # 4
    print(pow(98, 2))        # 9604
    print(pow(98, 0))        # 1
    print(pow(100, -2))      # 0.0001
    print(pow(-4, 5))        # -1024
