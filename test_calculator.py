# https://github.com/adamtanguf/lab10-AT-AT
# Partner 1: Adam Tang
# Partner 2: Adam Tang (solo)
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    # Partner 2 (me)
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 5), 4)
        self.assertEqual(add(-4, -6), -10)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(-3, -7), 4)
        self.assertEqual(subtract(0, 10), -10)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

    def test_logarithm(self):
        self.assertEqual(logarithm(10, 100), 2)
        self.assertEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(math.e, math.e**3), 3)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(1, 5)

    # Partner 1 (also me)
    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 5), -10)
        self.assertEqual(multiply(0, 100), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(7, 2), 3.5)
        self.assertEqual(divide(-12, -3), 4)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(2, -5)

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertEqual(hypotenuse(0, 0), 0)

    def test_sqrt(self):
        self.assertEqual(square_root(9), 3)
        self.assertAlmostEqual(square_root(2), math.sqrt(2))
        with self.assertRaises(ValueError):
            square_root(-1)

# Do not touch this
if __name__ == "__main__":
    unittest.main()
