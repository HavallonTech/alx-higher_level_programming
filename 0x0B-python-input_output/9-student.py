#!/usr/bin/python3
"""
Module for 9-student.py
Write a class Student that defines a student by:
"""


class Student:

    def __init__(self, first_name, last_name, age):
        """
          default method for all instance
        """
        Student.first_name = first_name
        Student.last_name = last_name
        Student.age = age

    def to_json(self):
        return self.__dict__
