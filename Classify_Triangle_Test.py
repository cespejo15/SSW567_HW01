import unittest
import math
from Classify_Triangle import BuggyTriangle

class TestTriangles(unittest.TestCase):
    def test_rightTriangle(self):
        """ test right triangle detection """
        self.assertTrue(BuggyTriangle(5, 12, 13).right_check())
        self.assertTrue(BuggyTriangle(3, 4, 5).right_check())
        self.assertTrue(BuggyTriangle(8, 8, math.sqrt(128)).right_check())

    def test_equilateralTriangles(self):
        """ test equilateral triangle detection """
        self.assertEqual(BuggyTriangle(7, 7, 7).classify_triangle(), "Equilateral Triangle")
        self.assertEqual(BuggyTriangle(5, 5, 5).classify_triangle(), "Equilateral Triangle")
        self.assertNotEqual(BuggyTriangle(1, 2, 3).classify_triangle(), "Equilateral Triangle")

    def test_isoscelesTriangles(self):
        """ test isosceles triangle detection """
        self.assertEqual(BuggyTriangle(4, 4, 6).classify_triangle(), "Isosceles Triangle")
        self.assertEqual(BuggyTriangle(2, 3, 2).classify_triangle(), "Isosceles Triangle")
        self.assertNotEqual(BuggyTriangle(6, 5, 3).classify_triangle(), "Isosceles Triangle")

    def test_scaleneTriangles(self):
        """ test scalene triangle detection """
        self.assertEqual(BuggyTriangle(4, 5, 6).classify_triangle(), "Scalene Triangle")
        self.assertEqual(BuggyTriangle(4, 7, 5).classify_triangle(), "Scalene Triangle")
        self.assertNotEqual(BuggyTriangle(5, 5, 3).classify_triangle(), "Scalene Triangle")

    def test_invalidTriangle(self):
        """ test invalid triangle detection """
        self.assertEqual(BuggyTriangle(9, 4, 4).classify_triangle(), "Invalid Triangle")
        self.assertEqual(BuggyTriangle(2, 7, 2).classify_triangle(), "Invalid Triangle")
        self.assertNotEqual(BuggyTriangle(3, 4, 5).classify_triangle(), "Invalid Triangle")


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
