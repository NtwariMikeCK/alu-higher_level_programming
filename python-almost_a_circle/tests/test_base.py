# tests/test_rectangle.py

import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """ Test cases for Rectangle class """

    def test_default_initialization(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_custom_initialization(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 5)

    def test_width_validation(self):
        with self.assertRaises(TypeError):
            r = Rectangle("1", 2)
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 2)

    def test_height_validation(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, "2")
        with self.assertRaises(ValueError):
            r = Rectangle(1, -2)

    def test_x_validation(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, "3")
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, -3)

    def test_y_validation(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, "4")
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, 3, -4)

    def test_area(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_str(self):
        r = Rectangle(3, 4, 1, 2, 5)
        self.assertEqual(str(r), "[Rectangle] (5) 1/2 - 3/4")

    def test_display(self):
        r = Rectangle(2, 2)
        with self.assertRaises(SystemExit):
            r.display()

    def test_to_dictionary(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.to_dictionary(), {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4})

    def test_update(self):
        r = Rectangle(1, 2)
        r.update(5, 6, 7, 8, 9)
        self.assertEqual(r.id, 5)
        self.assertEqual(r.width, 6)
        self.assertEqual(r.height, 7)
        self.assertEqual(r.x, 8)
        self.assertEqual(r.y, 9)

if __name__ == "__main__":
    unittest.main()
