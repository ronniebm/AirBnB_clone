#!/usr/bin/python3
"""file_storage.py module"""
from base_model import BaseModel
import json


class FileStorage():
    """
    FileStorage class:
    ------------------
    """
    __file.path = "file.json"
    __objects = {}

    def all(self):
        """
        public instance method that returns the
        dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        public instance method that sets in __objects
        the obj with key <obj class name>.id
        """
        if obj:
            key = str(type(obj).__name__)+"."+obj.id
            FileStorage.__objects[key] = obj

    def save(self):
        """
        public instance method that  serializes __objects
        to the JSON file (path: __file_path).
        """
        new_dict={}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file.path, mode='w') as my_file:
            json.dump(new_dict, my_file)

    def reload(self):
        pass
