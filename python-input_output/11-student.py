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

    def to_json(self, attrs=None):
        """
        this function retrieves a dictionary represents student but with attrs
        """
        if type(attrs) is list:
            new_obj = {}
            for key in attrs:
                if type(key) is str and key in self.__dict__:
                    new_obj[key] = self.__dict__[key]
            return new_obj
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        this function returns new version of obj which replaces all attributes
        """
        for key in json:
            self.__dict__[key] = json[key]
