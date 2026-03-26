#!/usr/bin/env python3
"""
this module contains with a function and this function
try to convert csv file to json format if is there any Exception
this function returns false otherwise returns true
"""


import csv
import json

def convert_csv_to_json(filename):
    """
    this function converts csv file to json format if
    is there any Exception function returns false otherwise
    returns true
    """
    try:    
        with open(filename, 'r', encoding="utf-8") as f:
            obj = list(csv.DictReader(f))
        with open("data.json", 'w', encoding="utf-8") as f:
            json.dump(obj, f)
        return True
    except Exception:
        return False
