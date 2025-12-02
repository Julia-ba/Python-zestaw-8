"""
Zadanie 6.2 z zestawu 6
testy do zadania znajduja sie w pliku test_points.py
"""

import math

class Point:
    """
    Klasa reprezentujaca punkty na plaszczyznie.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """
        Zwraca string w postaci (x, y).
        """
        return f'({self.x}, {self.y})'

    def __repr__(self):
        """
        Zwraca string Point(x, y).
        """
        return f'Point({self.x}, {self.y})'

    def __eq__(self, other):
        """
        Porownanie punktow.
        """
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        """
        Zwraca True, jesli punkty nie sa rowne.
        """
        return not self == other

    def __add__(self, other):
        """
        Dodawanie wektorow.
        """
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """
        Odejmowanie wektorow
        """
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        """
        Iloczyn skalarny.
        """
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        """
        Iloczyn wektorowy 2D (zwraca liczbe).
        """
        return self.x * other.y - self.y * other.x

    def length(self):
        """
        Dlugosc wektora od (0,0).
        """
        return math.hypot(self.x, self.y)

    def __hash__(self):
        """
        Pozwala uzywac Point w zbiorach i slownikach.
        """
        return hash((self.x, self.y))



