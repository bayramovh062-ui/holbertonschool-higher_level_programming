#!/usr/bin/env python3
"""
this module teaches  how to serialize and deserialize custom
Python objects using the pickle module.
"""


import pickle


class CustomObject():
    """
    this class creates an object with name, age, is_student parameters
    """
    def __init__(self, name, age, is_student):
        """
        this function initalizations parameters
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        this function displays object's information
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is student: {self.is_student}")

    def serialize(self, filename):
        """
        this function serializes object's data to a file
        with uing pickle
        """
        try:
            with open(filename, 'wb', encoding="utf-8") as f:
                pickle.dump(self, f)
        except exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        this function deserializes object from file with using pickle
        """
        try:
            with open(filename, 'rb', encoding="utf-8") as f:
                return pickle.load(f)
        except exception:
            return None
