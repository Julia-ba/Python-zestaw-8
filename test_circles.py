import pytest
from math import pi, sqrt, isclose
from circles import Circle
from points import Point

@pytest.fixture
def c1():
    return Circle(1, 2, 4)

@pytest.fixture
def p_basic():
    """Trzy punkty lezace na okregu jednostkowym."""
    return (Point(1, 0), Point(-1, 0), Point(0, 1))

@pytest.fixture
def p_collinear():
    """wspolliniowe punkty."""
    return (Point(0, 0), Point(5, 5), Point(10, 10))


def test_repr_and_equality(c1):
    assert repr(c1) == "Circle(1, 2, 4)"
    assert c1 == Circle(1, 2, 4)
    assert c1 != Circle(2, 3, 4)
    assert c1 != Circle(1, 2, 5)

def test_area(c1):
    assert isclose(c1.area(), pi * 16)
    assert isclose(Circle(0, 0, 0).area(), 0)

def test_move(c1):
    moved = c1.move(3, -1)
    assert moved.pt == Point(4, 1)
    assert moved.radius == 4
    assert c1.pt == Point(1, 2)

def test_invalid_radius():
    with pytest.raises(ValueError, match="Promień nie może być ujemny"):
        Circle(0, 0, -1)


def test_bounding_box_coordinates(c1):
    assert c1.top == 6
    assert c1.bottom == -2
    assert c1.left == -3
    assert c1.right == 5
    assert c1.width == 8
    assert c1.height == 8

def test_bounding_box_points(c1):
    assert c1.topleft == Point(-3, 6)
    assert c1.topright == Point(5, 6)
    assert c1.bottomleft == Point(-3, -2)
    assert c1.bottomright == Point(5, -2)


def test_from_points_unit_circle(p_basic):
    """Tworzenie okregu jednostkowego z trzech punktow."""
    circle = Circle.from_points(p_basic)
    assert isclose(circle.pt.x, 0, abs_tol=1e-9)
    assert isclose(circle.pt.y, 0, abs_tol=1e-9)
    assert isclose(circle.radius, 1, abs_tol=1e-9)

def test_from_points_shifted_triangle():
    """Okrag opisany na przesunietym trojkacie."""
    p1 = Point(1, 1)
    p2 = Point(3, 5)
    p3 = Point(-1, 5)
    circle = Circle.from_points((p1, p2, p3))
    assert isclose(circle.pt.x, 1.0, abs_tol=1e-9)
    assert isclose(circle.pt.y, 3.5, abs_tol=1e-9)
    assert isclose(circle.radius, 2.5, abs_tol=1e-9)

def test_from_points_collinear(p_collinear):
    """Blad, gdy punkty sa wspolliniowe."""
    with pytest.raises(ValueError, match="Punkty są współliniowe"):
        Circle.from_points(p_collinear)

def test_from_points_wrong_number():
    """Blad, gdy liczba punktow jest inna niz trzy."""
    with pytest.raises(ValueError, match="Należy podać dokładnie trzy punkty"):
        Circle.from_points((Point(1, 1), Point(2, 2)))
    with pytest.raises(ValueError, match="Należy podać dokładnie trzy punkty"):
        Circle.from_points((Point(1, 1), Point(2, 2), Point(3, 3), Point(4, 4)))


def test_cover_nonoverlapping():
    """Dwa nieprzecinajace sie okregi."""
    c1 = Circle(0, 0, 1)
    c2 = Circle(4, 0, 1)
    result = c1.cover(c2)
    assert isclose(result.pt.x, 2.0, abs_tol=1e-6)
    assert isclose(result.pt.y, 0.0, abs_tol=1e-6)
    assert isclose(result.radius, 3.0, abs_tol=1e-6)

def test_cover_contained():
    """Jeden okrag zawarty w drugim."""
    big = Circle(0, 0, 5)
    small = Circle(1, 1, 1)
    result = big.cover(small)
    assert result == big

def test_cover_identical():
    """Dwa identyczne okregi."""
    c1 = Circle(1, 2, 3)
    c2 = Circle(1, 2, 3)
    result = c1.cover(c2)
    assert result == c1
