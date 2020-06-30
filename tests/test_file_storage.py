#!/usr/bin/python3
"""File Storage test"""
import unittest
import json
import pep8
import models

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
        """Test that tests/test_file_storage.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_file_storage.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_doc_constructor(self):
        """Constructor documentation"""
        doc = FileStorage.__init__.__doc__
        self.assertGreater(len(doc), 1)

if __name__ == '__main__':
    unittest.main()
