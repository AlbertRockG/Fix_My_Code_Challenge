#!/usr/bin/python3
"""Defines a class named Square"""


class square():
    """Represents a Square.

    Args:
        width (int): The width of the square.
        height (int): The height of the height.
    """
    width = 0
    height = 0

    
    def __init__(self, *args, **kwargs):
        """Initialize a new square"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """Perimeter of the square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """Return a printable of format of the square"""
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())