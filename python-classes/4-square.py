#!/usr/bin/python3
"""
innitialization
"""


class Square:
    """
    creating the square class
    """
    def __init__(self, size=0):
        """
        assigning the private instance attribute
        """
        self.size = size  # This will invoke the setter method to ensure validation

    @property
    def size(self):
        """
        assigning the gettor operator
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        assigning the settor operator
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        creating a public class attribute
        """
        return self.__size * self.__size
