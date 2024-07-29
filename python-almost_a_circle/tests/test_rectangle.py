import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_area(self):
        r = Rectangle(10, 2)
        self.assertEqual(r.area(), 20)

    def test_width(self):
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)

    def test_height(self):
        r = Rectangle(10, 2)
        self.assertEqual(r.height, 2)

    # Add more tests as needed


if __name__ == '__main__':
    unittest.main()
