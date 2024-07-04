#!/usr/bin/python3
"""
Defining which interpreter to run the below code
"""



class Square:
    """
    defining the class
    """
    def __init__(self, size=0):
        """
        checking for correct value to ensure there no errors
        """
        """
        creating a private instance attribute
        """
        self.size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
    def area(self):
        """
        creating a public class attribute
        """
        area = self.size * self.size
        return area
