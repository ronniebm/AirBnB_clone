#!/usr/bin/python3
"""Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class implementation"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """User constructor"""
        super().__init__(*args, **kwargs)
