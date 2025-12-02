"""
Zadanie 8.3 z zestawu 8
testy do zadania znajduja sie w pliku test_circles.py
"""

from math import pi, sqrt
from points import Point

class Circle:
    """
    Klasa reprezentujaca okregi na plaszczyznie.
    """

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("Promień nie może być ujemny.")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):
        """
        Zwraca string 'Circle(x, y, radius)'.
        """
        return f"Circle({self.pt.x}, {self.pt.y}, {self.radius})"

    def __eq__(self, other):
        """
        Zwraca True, jesli okregi maja ten sam srodek i promien.
        """
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        """
        Zwraca True, jesli okregi są rozne.
        """
        return not self == other

    def area(self):
        """
        Zwraca pole powierzchni okregu.
        """
        return pi * self.radius ** 2

    def move(self, x, y):
        """
        Zwraca nowy okrag przesuniety o (x, y).
        """
        return Circle(self.pt.x + x, self.pt.y + y, self.radius)

    def cover(self, other):
        """
        Zwraca najmniejszy okrag pokrywajacy oba okregi.
        """
        d = sqrt((self.pt.x - other.pt.x) ** 2 + (self.pt.y - other.pt.y) ** 2)

        if self.radius >= d + other.radius:
            return Circle(self.pt.x, self.pt.y, self.radius)
        if other.radius >= d + self.radius:
            return Circle(other.pt.x, other.pt.y, other.radius)

        new_radius = (d + self.radius + other.radius) / 2

        r = (new_radius - self.radius) / d
        new_x = self.pt.x + r * (other.pt.x - self.pt.x)
        new_y = self.pt.y + r * (other.pt.y - self.pt.y)

        return Circle(new_x, new_y, new_radius)

    @classmethod
    def from_points(cls, points):
        """
        Tworzy okrag przechodzacy przez trzy punkty (circumcircle).
        """
        if len(points) != 3:
            raise ValueError("Należy podać dokładnie trzy punkty.")

        p1, p2, p3 = points

        A = p2.x - p1.x
        B = p2.y - p1.y
        C = p3.x - p1.x
        D = p3.y - p1.y

        E = A * (p1.x + p2.x) + B * (p1.y + p2.y)
        F = C * (p1.x + p3.x) + D * (p1.y + p3.y)
        G = 2 * (A * (p3.y - p2.y) - B * (p3.x - p2.x))

        if abs(G) < 1e-10:
            raise ValueError("Punkty są współliniowe – nie można utworzyć okręgu.")

        cx = (D * E - B * F) / G
        cy = (A * F - C * E) / G
        center = Point(cx, cy)

        radius = sqrt((center.x - p1.x) ** 2 + (center.y - p1.y) ** 2)
        return cls(center.x, center.y, radius)


    @property
    def top(self):
        return self.pt.y + self.radius

    @property
    def bottom(self):
        return self.pt.y - self.radius

    @property
    def left(self):
        return self.pt.x - self.radius

    @property
    def right(self):
        return self.pt.x + self.radius

    @property
    def width(self):
        return 2 * self.radius

    @property
    def height(self):
        return 2 * self.radius

    @property
    def topleft(self):
        return Point(self.left, self.top)

    @property
    def topright(self):
        return Point(self.right, self.top)

    @property
    def bottomleft(self):
        return Point(self.left, self.bottom)

    @property
    def bottomright(self):
        return Point(self.right, self.bottom)

