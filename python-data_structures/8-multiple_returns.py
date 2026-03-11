#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first_element = None
    if length != 0:
        first_element = sentence[0]
    new_tuple = (length, first_element)
    return new_tuple
