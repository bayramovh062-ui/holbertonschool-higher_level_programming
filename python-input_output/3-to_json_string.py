#!/usr/bin/python3
"""
this module contains python code which
teaches you how to convert python object to json
format
"""

import json


def to_json_string(my_obj):
    """
    this function returns json format of my_obj
    """
    return json.dumps(my_obj)
