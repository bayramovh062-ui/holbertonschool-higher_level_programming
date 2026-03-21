#!/usr/bin/python3
"""
this module checks that same class or not
"""


def is_same_class(obj, a_class):
    """
    this function checks that obj in the class or not
    """
    if isinstance(obj, a_class):
        return True
    return False
