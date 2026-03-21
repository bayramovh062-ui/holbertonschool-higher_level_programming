#!/usr/bin/python3
"""
This module contains a function that checks if an object is an instance of a class
that inherited (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherited
    from a_class, but not if obj is exactly an instance of a_class.
    """

    return isinstance(obj, a_class) and type(obj) is not a_class
