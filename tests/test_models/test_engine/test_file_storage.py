#!/usr/bin/python3
"""File Storage test"""
import unittest
import json
import pep8
import models
import os
import sys

from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage"""

    def test_doc_module(self):
        """Module documentation"""
        doc = FileStorage.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_file_storage(self):
        """Test that models/engine/file_storage.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_file_storage(self):
        """Test that tests/test_models/test_engine/test_file_storage.py
        conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        val = 'tests/test_models/test_engine/test_file_storage.py'
        res = pep8style.check_files([val])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_doc_constructor(self):
        """Constructor documentation"""
        doc = FileStorage.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_init(self):
        """Test constructor"""
        f = FileStorage()
        obj, path = f._FileStorage__objects, f._FileStorage__file_path

        self.assertIsInstance(obj, dict)
        self.assertIsInstance(path, str)

    def test_functions(self):
        """Checks if the functions are defined"""
        f = FileStorage()

        self.assertTrue(hasattr(f, 'all'))
        self.assertTrue(hasattr(f, 'new'))
        self.assertTrue(hasattr(f, 'reload'))
        self.assertTrue(hasattr(f, 'save'))

    def test_all(self):
        """Test method all"""
        f = FileStorage()

        self.assertIsInstance(f.all(), dict)

    def test_example(self):
        """Checks the methods reload and save"""
        # Needs to be implemented
        from models import storage
        from models.base_model import BaseModel

        f = FileStorage()
        storage.all()
        status = os.path.exists(f._FileStorage__file_path)
        self.assertTrue(status)

        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        my_model.save()

    def test_file_existence(self):
        """
        Checks if methods from Storage Engine works.
        """

        with open("file.json") as f:
            self.assertTrue(len(f.read()) > 0)

if __name__ == '__main__':
    unittest.main()
