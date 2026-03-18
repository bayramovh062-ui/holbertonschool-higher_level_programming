#!/usr/bin/python3
"""
This is the "5-text_indentation" module.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    text = text.strip()
    
    skip_space = False
    for char in text:
        if skip_space and char == ' ':
            continue
        
        skip_space = False
        print(char, end="")
        
        if char in ".?:":
            print("\n")
            skip_space = True
