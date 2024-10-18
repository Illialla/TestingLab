import unittest
from main import find_roots

class TestStringMethods(unittest.TestCase):
    def test_find_roots(self):
        assert find_roots(1, 5, 6) == (-2.0, -3.0)

    def test_one_root(self):
        assert find_roots(1, 2, 1) == (-1.0)

    def test_complex_roots(self):
        assert find_roots(1, 2, 5) == (-1 + 2j, -1 - 2j)

    def test_division_by_zero(self):
        assert find_roots(0, 2, 3) == "Деление на 0!"
        # try:
        #     find_roots(0, 2, 3)
        # except ZeroDivisionError:
        #     pass  # Ожидаем ошибку деления на ноль

    def test_null_b(self):
        assert find_roots(1, 0, -4) == (2.0, -2.0)

    def test_negative_nums(self):
        assert find_roots(-1, -4, -4) == (-2.0)

    def test_big_ints(self):
        assert find_roots(10 ** 6, 10 ** 6, 10 ** 6)

    def test_not_enough_args(self):
        with self.assertRaises(TypeError):
            find_roots(1, 2)

    def test_wrong_arg_type(self):
        with self.assertRaises(TypeError):
            find_roots("a", 1, 2)

if __name__ == '__main__':
    unittest.main()
