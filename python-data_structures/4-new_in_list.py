#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx >= 0 and idx < len(my_list):
        new_list = my_list
        my_list[idx] = element
        new_list = my_list
    return new_list
