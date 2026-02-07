import math


class Geometry:
    """Obliczanie pól i obwodów figur geometrycznych: Prostokąt, Kwadrat, Okrąg, Trójkąt"""

    # Prostokąt

    def rectangle_area(self, width, height):
        if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
            raise TypeError("To nie jest wartość liczbowa")
        if width <= 0 or height <= 0:
            raise ValueError("Wartośc liczbowa musi być dodatnia")
        return width * height

    def rectangle_perimeter(self, width, height):
        if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
            raise TypeError("To nie jest wartość liczbowa")
        if width <= 0 or height <= 0:
            raise ValueError("Wartośc liczbowa musi być dodatnia")
        return 2 * (width + height)

    # Kwadrat

    def square_area(self, side):
        if not isinstance(side, (int, float)):
            raise TypeError("To nie jest wartość liczbowa")
        if side <= 0:
            raise ValueError("Wartośc liczbowa musi być dodatnia")
        return side**2

    def square_perimeter(self, side):
        if not isinstance(side, (int, float)):
            raise TypeError("To nie jest wartość liczbowa")
        if side <= 0:
            raise ValueError("Wartośc liczbowa musi być dodatnia")
        return 4 * side

    # Okrąg

    def circle_area(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError("To nie jest wartość liczbowa")
        if radius <= 0:
            raise ValueError("Wartośc liczbowa musi być dodatnia")
        return math.pi * radius**2

    def circle_circumference(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError("To nie jest wartość liczbowa")
        if radius <= 0:
            raise ValueError("Wartośc liczbowa musi być dodatnia")
        return 2 * math.pi * radius

    # Trójkąt

    def triangle_area(self, base, height):
        if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
            raise TypeError("To nie jest wartość liczbowa")
        if base <= 0 or height <= 0:
            raise ValueError("Wartośc liczbowa musi być dodatnia")
        return 0.5 * base * height

    def triangle_perimeter(self, a, b, c):
        if not all(isinstance(x, (int, float)) for x in (a, b, c)):
            raise TypeError("To nie jest wartość liczbowa")
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Wartośc liczbowa musi być dodatnia")
        return a + b + c
