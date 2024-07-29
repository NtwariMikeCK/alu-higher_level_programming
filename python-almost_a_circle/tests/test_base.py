# tests/test_base.py

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """ Test cases for the Base class. """

    def test_default_id(self):
        b = Base()
        self.assertEqual(b.id, 1)

    def test_custom_id(self):
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_id_increment(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, 2)

if __name__ == '__main__':
    unittest.main()
