#!/usr/bin/env python3
"""
this module adds the functionality to serialize a Python dictionary to a
JSON file and deserialize the JSON file to recreate the Python Dictionary.
"""


import json


def serialize_and_save_to_file(data, filename):
    """
    this function serializes data and saves this data  to a file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    this function deserializes data to a file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
