#!/usr/bin/python3
"""
this module checks that same class or not
"""


def is_same_class(obj, a_class):
    """
    this function checks that obj in the class or not
    """
    return type(obj) is a_class
