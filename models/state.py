#!/usr/bin/python3
"""State class"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class implementation"""
    name = ""

    def __init__(self, *args, **kwargs):
        """State constructor"""
        super().__init__(*args, **kwargs)
