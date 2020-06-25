#!/usr/bin/python3
"""base_model.py module"""
import uuid

class BaseModel():
    """
    BaseModel class:
    ----------------
    It defines all common attributes/methods
    for the other classes.
    """

    def __init__(self, id=None):
        """
        This is the constructor.

        Arguments:
        ---------
        id [object] -- UUID generated with python uuid.
        """
        self.id = uuid.uuid4()


juan = BaseModel()
print(juan.id)
