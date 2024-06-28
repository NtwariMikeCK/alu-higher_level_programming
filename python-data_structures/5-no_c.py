#!/usr/bin/python3
def no_c(my_string):
    # Initialize an empty string to store the new string without 'c' and 'C'
    new_string = ""

    # Iterate over each character in the original string
    for char in my_string:
        # Append the character to the new string if it is not 'c' or 'C'
        if char != 'c' and char != 'C':
            new_string += char

    return new_string

# Sample usage:
if __name__ == "__main__":
    print(no_c("Best School"))  # Output: Best Shool
    print(no_c("Chicago"))      # Output: hiago
    print(no_c("C is fun!"))    # Output:  is fun!

