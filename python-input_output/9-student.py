#!/usr/bin/python3
"""
this module contains a class and this class create
new student object and returns json format of object
"""


class Student():
    """
    this class represents student
    """
    def __init__(self, first_name, last_name, age):
        """
        this function will intialization values when user create a new object
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        this function retrieves a dictionary represents student
        """
        return self.__dict__
