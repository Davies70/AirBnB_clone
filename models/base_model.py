#!/usr/bin/python3

""" base module """


from datetime import datetime
from uuid import uuid4
import models


class BaseModel:

    """ defines all common attributes/methods for other classes """

    def __init__(self, *args, **kwargs):

        """ initializing the class with constructor """

        self.updated_at = datetime.today()
        self.id = str(uuid4())
        self.created_at = datetime.today()

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    date = value[0:10] + " " + value[11:]
                    self.created_at = datetime.strptime(
                        date, '%Y-%m-%d %H:%M:%S.%f')
                elif key == "updated_at":
                    date = value[0:10] + " " + value[11:]
                    self.updated_at = datetime.strptime(
                        date, "%Y-%m-%d %H:%M:%S.%f")
                elif key != "__class__":
                    setattr(self, key, value)
        models.storage.new(self)

    def __str__(self):
        """ defining string representation of class """

        return ("[{}] ({}) {}"
                .format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):

        """ updating the datetime of object change
            and saving the json object to file
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):

        """ creating a dictionary format of the class """

        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['created_at'] = self.created_at.isoformat()
        return my_dict
