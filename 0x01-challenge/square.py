#!/usr/bin/python3
"""Defines a class named Square."""


class Square():
    """Represents a Square.
    Args:
        size (int): The height of the square.
    """
    size = 0

    def __init__(self, *args, **kwargs):
        """Initialize a new square."""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.size * self.size

    def permiterOfMySquare(self):
        """Perimeter of the square"""
        return (self.size * 2) + (self.size * 2)

    def __repr__(self):
        """Return a printable of format of the square"""
        return "{}/{}".format(self.size, self.size)


if __name__ == "__main__":
    """Create Square instance """
    s = Square(width=12)
    print(s)
    print(s.area_of_my_square())
    print(s.permiterOfMySquare())
