#!/usr/bin/python3
"""
This module defines a class Square.
"""


class Square:
    """
    Represents a square.

    Attributes:
        __size (int): The size of the square.
    """
    def __init__(self, size=0):
         """
        Initializes a new square.

        Args:
            size (int): The size of the square.
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size  # This will invoke the setter method to ensure validation

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
    
    def my_print(self):
        """
        This checks if size is 0 and returns empty str.

        else:
            prints # * size in the range of size        
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
