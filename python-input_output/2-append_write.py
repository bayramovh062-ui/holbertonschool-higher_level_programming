#!/usr/bin/python3
"""
this module explains how to add a text to a file
using pythons's write command with a mode
"""


def append_file(filename="", text=""):
    """
    this functipn append text to a file and
    returns number of characthers added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
