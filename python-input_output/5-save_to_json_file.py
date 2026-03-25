#!/usr/bin/python3
"""
this module teaches that how can you save an object to a file
with using json representations
"""


import json


def save_to_json_file(my_obj, filename):
    """
    this function save object to a file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
