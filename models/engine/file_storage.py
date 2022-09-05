#!/usr/bin/python3

""" FileStorage Module """

import json
from models.base_model import BaseModel


class FileStorage:
    """  serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """

        O_cls = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(O_cls, obj.id)] = obj.__dict__

    def save(self):
        """  serializes __objects to the JSON file """
        with open(FileStorage.__file_path, "+w") as f:
            json.dump(FileStorage.__objects, f, default=str)

    def reload(self):
        """ deserializes the JSON file to __objects """

        FileStorage.__objects = {}
        try:
            with open(FileStorage.__file_path,
                      mode="r+", encoding="utf-8") as fd:
                FileStorage.__objects = json.load(fd)
        except Exception as e:
            return
