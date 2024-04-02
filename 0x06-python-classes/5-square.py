#!/usr/bin/python3
"""A module that declares a class"""


class Square:
    """a class that defines a square"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        return self.__size**2

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def my_print(self):
        value = self.__size
        for i in range(value):
            [print('#', end='') for j in range(value)]
            print('')
        if value == 0:
            print('')
