#!/usr/bin/python3
"""Module for test BaseModel class"""
import unittest
import json

from models import base_model


class TestBaseModel(unittest.TestCase):
    """Test for BaseModel class"""

    def test_doc_module(self):
        """Module documentation"""
        doc = base_model.BaseModel.__doc__
        self.assertGreater(len(doc), 1)

    def test_doc_class(self):
        """BaseModel documentation"""
        doc = base_model.BaseModel.__doc__
        self.assertGreater(len(doc), 1)

    def test_doc_constructor(self):
        """Constructor documentation"""
        doc = base_model.BaseModel.__init__.__doc__
        self.assertGreater(len(doc), 1)
