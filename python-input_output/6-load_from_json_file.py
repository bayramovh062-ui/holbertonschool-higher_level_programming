#!/usr/bin/python3
"""
this module contains convert json file to
python object and writes a file codes
"""

import json


def load_from_json_file(filename):
    """
    this function convert json file to
    python object and writes a file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
