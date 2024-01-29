import unittest
import math


class BuggyTriangle:
    def __init__(self, s1, s2, s3):
        self.a = s1
        self.b = s2
        self.c = s3

    def right_check(self):
        x = round(self.a ** 2, 4)
        y = round(self.b ** 2, 4)
        z = round(self.c ** 2, 4)
        if x + y == z:
            return True
        else:
            return False

    def classify_triangle(self):
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            return "Invalid Triangle"
        elif self.a == self.b:
            if self.b == self.c:
                return "Equilateral Triangle"
            elif self.b != self.c:
                triangle = "Isosceles Triangle"
                if self.right_check():
                    triangle = triangle + " and Right Triangle"
                return triangle
        elif self.a != self.b:
            if self.b == self.c or self.a == self.c:
                triangle = "Isosceles Triangle"
                if self.right_check():
                    triangle = triangle + " and Right Triangle"
                return triangle
            elif self.b != self.c:
                triangle = "Scalene Triangle"
                if self.right_check():
                    triangle = triangle + " and Right Triangle"
                return triangle


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
