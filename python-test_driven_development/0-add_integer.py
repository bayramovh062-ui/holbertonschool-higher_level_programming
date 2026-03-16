#!/usr/bin/python3
"""
This is the "0-add_integer" module.

The 0-add_integer module supplies one function, add_integer(a, b).
This function adds two numbers and returns an integer.
"""


def add_integer(a, b=98):
    """
    Returns the integer addition of a and b.
    Float arguments are typecasted to ints before addition.
    Raises TypeError if a or b are not integers or floats.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
