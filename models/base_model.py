#!/usr/bin/python3
"""base_model.py module"""
import uuid
from datetime import datetime


class BaseModel():
    """
    BaseModel class:
    ----------------
    It defines all common attributes/methods
    for the other classes.

    """

    def __init__(self, *args, **kwargs):
        """
        This is the constructor.

        Arguments:
        ---------
        id [str] -- UUID generated with python uuid.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(value,
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(value,
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    if key != "__class__":
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """str representation of the base class."""
        msg = ("[{}] ({}) {}".format(self.__class__.__name__,
               self.id, self.__dict__))
        return msg

    def save(self):
        """
        This method updates the instance attribute
        'self.udated_at'.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        This method creates a new dictionary:
        -------------------------------------
        Key: {created_at} -- was converted to string isoformat().
        Key: {updated_at} -- was converted to string isoformat().
        Key: {__class__}  -- was added, it contains the class name.
        """
        new_dict = dict(self.__dict__)
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return (new_dict)
