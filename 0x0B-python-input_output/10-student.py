#!/usr/bin/python3
"""
Module for 10-student.py
Write a class Student that defines a student by: (based on 9-student.py)
"""


class Student:

    def __init__(self, first_name, last_name, age):
        """
          default method for all instance
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        desired_key = 'name'
        if (isinstance(attrs, list)) and all(isinstance(x_in_attrs, str) for x_in_attrs in attrs):
            return {e: getattr(self, e) for e in attrs if hasattr(self, e)}            
        else:
            return (self.__dict__)
