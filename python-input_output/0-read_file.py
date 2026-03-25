#!/usr/bin/python3
"""
this module contains a function that explains
read file with python code
"""


def read_file(filename=""):
    """
    this function reads file
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read())
