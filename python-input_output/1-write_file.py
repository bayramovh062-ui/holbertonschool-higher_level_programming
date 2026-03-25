#!/usr/bin/python3
"""
this module explains write files with using function
"""


def write_file(file_name="", text=""):
    """
    this function write text to file and return length of text
    """
    with open(filename, 'w', encoding = "utf-8") as f:
        f.write(text)
    return len(text)

