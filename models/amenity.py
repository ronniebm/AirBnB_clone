#!/usr/bin/python3
"""Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class implementation"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Amenity constructor"""
        super().__init__(*args, **kwargs)
