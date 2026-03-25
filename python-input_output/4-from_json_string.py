#!/usr/bin/python3
"""
this module teaches that how to convert json to python
"""


import json


def from_json_string(my_str):
    """
    this function return json object's  python format
    """
    return json.loads(my_str)
