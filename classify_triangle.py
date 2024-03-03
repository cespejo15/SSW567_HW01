"""Triangle Classification Function"""
class BuggyTriangle:
    """Constructor"""
    def __init__(self, s1, s2, s3):
        self.a = s1
        self.b = s2
        self.c = s3

    def right_check(self):
        """Checks if a Triangle contains a right angle, returns false if otherwise"""
        x = round(self.a ** 2, 4)
        y = round(self.b ** 2, 4)
        z = round(self.c ** 2, 4)
        return bool(x + y == z)

    def classify_triangle(self):
        """Classifies triangle and type"""
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            return "Invalid Triangle"
        if self.a == self.b:
            if self.b == self.c:
                return "Equilateral Triangle"
            if self.b != self.c:
                triangle = "Isosceles Triangle"
                if self.right_check():
                    triangle = triangle + " and Right Triangle"
                return triangle
        if self.a != self.b:
            if self.c in (self.a, self.b):
                triangle = "Isosceles Triangle"
                if self.right_check():
                    triangle = triangle + " and Right Triangle"
                return triangle

        triangle = "Scalene Triangle"
        if self.right_check():
            triangle = triangle + " and Right Triangle"
        return triangle
        