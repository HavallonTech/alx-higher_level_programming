#!/usr/bin/python3
"""
module for base.py
"""


import json
class Base:
    """private class attribute 
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Init method always called when an instance is raise
        Args:
            id (int, optional): Assignef to the id attribute.
            otherwise, increments __nb_objects and assigns the new value to id.
        """
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """The to_Json method
        Args: 
            Accepts a list dictionary and 
        Return:
            a Json string representation of the list
            This implies dumps would be used
        """
        if (list_dictionaries == None):
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """A method to save the Json object to a file
        Args:
            cls: class name
            list_objs: list of instance 
        """
        ff = f"{cls.__name__}.json"
        if (list_objs == None):
            list_objs = []
            
        obj_details_list = [obj.to_dictionary() for obj in list_objs]
        json_data = cls.to_json_string(obj_details_list)
        with open(ff, 'w') as file:
            file.write(json_data)
    
    @staticmethod
    def from_json_string(json_string):
        """The from_Json_string method
        Return:
            a list of Json string representation
            This implies loads would be used
        """
        if (json_string == None):
            return ([])
        else:
            return (json.loads(json_string))
        
    