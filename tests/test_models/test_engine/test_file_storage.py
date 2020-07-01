#!/usr/bin/python3
import unittest
import pep8
from models.engine.file_storage import FileStorage
from models.__init__ import storage
from models.base_model import BaseModel


def setUpModule():
    """SetUpModule """
    pass


def tearDownModule():
    """tearDownModule """
    pass


class TestStringMethods(unittest.TestCase):
    """ Check the pep8 """
    def testpep8(self):
        style = pep8.StyleGuide(quiet=True)
        file1 = "models/engine/file_storage.py"
        file2 = "tests/test_models/test_engine/test_file_storage.py"
        check = style.check_files([file1, file2])
        self.assertEqual(check.total_errors, 0,
                         "Found code style errors (and warning).")


class TestModels(unittest.TestCase):

    def setUp(self):
        """ Set a variable """
        self.my_model = BaseModel()
        self.fisto = FileStorage()
        print("setUp")

    def tearDown(self):
        """ End variable """
        print("tearDown")

    @classmethod
    def setUpClass(cls):
        """ Set a Class """
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        """ Del a Class"""
        print("tearDownClass")

    def test_file_storage_doc(self):
        """ Check the documentation """
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.__init__.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_fiel_storage_exist(self):
        """ Check if methods exists """
        self.assertTrue(hasattr(self.fisto, "__init__"))
        self.assertTrue(hasattr(self.fisto, "all"))
        self.assertTrue(hasattr(self.fisto, "new"))
        self.assertTrue(hasattr(self.fisto, "save"))
        self.assertTrue(hasattr(self.fisto, "reload"))

    def test_models_save(self):
        """ Check if the save function works """
        self.my_model.name = "Halo"
        self.my_model.save()
        storage.reload()
        storage.all()
        self.assertTrue(storage.all(), "Halo")
        self.assertTrue(hasattr(self.my_model, 'save'))
        self.assertNotEqual(self.my_model.created_at,
                            self.my_model.updated_at)


if __name__ == '__main__':
    unittest.main()
