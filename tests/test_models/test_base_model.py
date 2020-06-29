#!/usr/bin/python3
"""Module for test BaseModel class"""
import unittest
import json

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test for BaseModel class"""

    def test_doc_module(self):
        """Module documentation"""
        doc = BaseModel.__doc__
        self.assertGreater(len(doc), 1)

    def test_doc_class(self):
        """BaseModel documentation"""
        doc = BaseModel.__doc__
        self.assertGreater(len(doc), 1)

    def test_doc_constructor(self):
        """Constructor documentation"""
        doc = BaseModel.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_first_task(self):
        """Test creation of class"""
        my_model = BaseModel()
        self.assertIs(type(my_model), BaseModel)
        my_model.name = "Holberton"
        my_model.my_number = 89
        self.assertEqual(my_model.name, "Holberton")
        self.assertEqual(my_model.my_number, 89)

        second_model = BaseModel()
        self.assertIs(type(second_model), BaseModel)
        second_model.name = "Andres"
        second_model.my_number = 80
        self.assertEqual(second_model.name, "Andres")
        self.assertEqual(second_model.my_number, 80)

if __name__ == '__main__':
    unittest.main()
