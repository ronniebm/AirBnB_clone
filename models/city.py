#!/usr/bin/python3
"""city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """City Class implementation"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """City class constructor"""
        super().__init__(*args, **kwargs)
