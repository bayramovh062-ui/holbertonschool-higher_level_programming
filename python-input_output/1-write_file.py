#!/usr/bin/python3
"""
this module explains write files with using function
"""


def write_file(filename="", text=""):
    """
    this function write text to file and return length of text
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
