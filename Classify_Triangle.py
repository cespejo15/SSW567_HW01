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
