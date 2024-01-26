def classify_triangle(a, b, c):
    if a^2 + b^2 == c^2:
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