#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for idx, num in enumerate(row):
            if idx < len(row) - 1:
                print("{:d}".format(num), end=" ")
            else:
                print("{:d}".format(num), end="")
        print()  # New line at the end of each row


# Sample usage:
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print_matrix_integer(matrix)
    print("--")
    print_matrix_integer()
