import pytest

from operations import multiply, divide, add, subtract, power, square_root


class TestOperations:

    def test_add(self):
        assert add(2, 3) == 5

    def test_subtract(self):
        assert subtract(5, 2) == 3

    def test_multiply(self):
        assert multiply(4, 3) == 12

    def test_divide(self):
        assert divide(10, 2) == 5
        assert divide(10, 0) == "Błąd: dzielenie przez zero"

    def test_power(self):
        assert power(2, 3) == 8

    def test_square_root(self):
        assert square_root(16) == 4
        assert square_root(-2) == "Błąd: liczba ujemna"


