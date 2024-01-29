import unittest

def classify_triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        print("Invalid Triangle")
        return
    elif a^2 + b^2 == c^2:
        triangle = "Right Triangle and "
    else:
        triangle = ""
    if a == b:
        if b == c:
            print(triangle + "Equilateral Triangle")
        elif b != c:
            print(triangle + "Isosceles Triangle")
    elif a!= b:
        if b == c:
            print(triangle + "Isosceles Triangle")
        elif b != c:
            print(triangle + "Scalene Triangle")

classify_triangle(2, 2, 2)
classify_triangle(3, 4, 5)
classify_triangle(6, 3, 2)
    
class TestTriangles(unittest.TestCase):
    def test_rightTriangle(self):
        self.assertEqual(classify_triangle(5, 12, 13), "Right Triangle and ")
        self.assertEqual(classify_triangle(3, 4, 5), "Right Triangle and ")
        self.assertNotEqual(classify_triangle(7, 8, 3), "Right Triangle and ")

    def test_equilateralTriangles(self):
        self.assertEqual(classify_triangle(7, 7, 7), "Equilateral Triangle")
        self.assertEqual(classify_triangle(5, 5, 5), "Equilateral Triangle")
        self.assertNotEqual(classify_triangle(1, 2, 3), "Equilateral Triangle")

    def test_isoscelesTriangles(self):
        self.assertEqual(classify_triangle(4, 4, 6), "Isosceles Triangle")
        self.assertEqual(classify_triangle(2, 7, 2), "Isosceles Triangle")
        self.assertNotEqual(classify_triangle(6, 5, 3), "Isosceles Triangle")

    def test_scaleneTriangles(self):
        self.assertEqual(classify_triangle(4, 4, 6), "Scalene Triangle")
        self.assertEqual(classify_triangle(5, 7, 5), "Scalene Triangle")
        self.assertNotEqual(classify_triangle(6, 5, 3), "Scalene Triangle")

    def test_invalidTriangle(self):
        self.assertEqual(classify_triangle(9, 4, 4), "Invalid Triangle")
        self.assertEqual(classify_triangle(2, 7, 2), "Invalid Triangle")
        self.assertNotEqual(classify_triangle(3, 4, 5), "Invalid Triangle")

        
# if __name__ == ‘__main__’:
#     unittest.main(exit=True)
