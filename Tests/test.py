import unittest
from main import find_roots

class TestStringMethods(unittest.TestCase):
    def test_find_roots1(self):
        assert find_roots(1, 5, 6) == (-2.0, -3.0)

    def test_find_roots2(self):
        assert find_roots(1, 2, 1) == (-1.0, -1.0)

    def test_find_roots3(self):
        assert find_roots(1, 2, 5) == (-1 + 2j, -1 - 2j)

    def test_find_roots4(self):
        try:
            find_roots(0, 2, 3)
        except ZeroDivisionError:
            pass  # Ожидаем ошибку деления на ноль

    def test_find_roots5(self):
        assert find_roots(1, 0, -4) == (2.0, -2.0)

    def test_find_roots6(self):
        assert find_roots(-1, -4, -4) == (-2.0, -2.0)

    def test_find_roots7(self):
        assert find_roots(10 ** 6, 10 ** 6, 10 ** 6)

if __name__ == '__main__':
    unittest.main()
