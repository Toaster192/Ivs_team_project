# merioneslib_tests.py
# Projekt IVS II.
# Autor: Jaromír Wysoglad, xwysog00
# Datum: 2018-03-26

import unittest

from src.merionesmathlib import Merioneslib

# To run tests, go to the parent directory and
# type "python3 -m tests.merioneslib_tests.py"

class MerioneslibTestAdd(unittest.testcase):
    def setUp(self):
        self.math = Merioneslib()

    def test_add_positive(self):
        self.assertEqual(self.math.add(1, 2), 3)
        self.assertEqual(self.math.add(0, 0), 0)
        self.assertEqual(self.math.add(0, 2), 2)
        self.assertEqual(self.math.add(58, 72), 130)

    def test_add_negative(self):
        self.assertEqual(self.math.add(-1, -1), -2)
        self.assertEqual(self.math.add(0, -5), -5)
        self.assertEqual(self.math.add(-5, 0), -5)
        self.assertEqual(self.math.add(-58, -72), -130)

    def test_add_positive_negative(self):
        self.assertEqual(self.math.add(-5, 2), -3)
        self.assertEqual(self.math.add(5, -7), -2)
        self.assertEqual(self.math.add(-7, 8), 1)
        self.assertEqual(self.math.add(-7, 7), 0)

    def test_add_decimal(self):
        self.assertEqual(self.math.add(2.25, 4.5), 6.75)
        self.assertEqual(self.math.add(-2.25, 4.5), 2.25)
        self.assertEqual(self.math.add(-2.25, -4.5), -6.75)


class MerioneslibTestSub(unittest.testcase):
    def setUp(self):
        self.math = Merioneslib()

    def test_sub_positive(self):
        self.assertEqual(self.math.sub(1, 2), -1)
        self.assertEqual(self.math.sub(0, 0), 0)
        self.assertEqual(self.math.sub(0, 2), -2)
        self.assertEqual(self.math.sub(72, 58), 14)

    def test_sub_negative(self):
        self.assertEqual(self.math.sub(-1, -1), 0)
        self.assertEqual(self.math.sub(0, -5), 5)
        self.assertEqual(self.math.sub(-5, 0), -5)
        self.assertEqual(self.math.sub(-58, -72), 14)

    def test_sub_positive_negative(self):
        self.assertEqual(self.math.sub(-5, 2), -7)
        self.assertEqual(self.math.sub(5, -7), 12)
        self.assertEqual(self.math.sub(-7, 8), -15)
        self.assertEqual(self.math.sub(7, 8), -1)

    def test_sub_decimal(self):
        self.assertEqual(self.math.sub(2.25, 4.5), -2.25)
        self.assertEqual(self.math.sub(-2.25, 4.5), -6.75)
        self.assertEqual(self.math.sub(-2.25, -4.5), 2.25)


class MerioneslibTestMul(unittest.testcase):
    def setUp(self):
        self.math = Merioneslib()

    def test_mul_positive(self):
        self.assertEqual(self.math.mul(1, 2), 2)
        self.assertEqual(self.math.mul(0, 0), 0)
        self.assertEqual(self.math.mul(0, 2), 0)
        self.assertEqual(self.math.mul(72, 58), 4176)

    def test_mul_negative(self):
        self.assertEqual(self.math.mul(-1, -1), 1)
        self.assertEqual(self.math.mul(0, -5), 5)
        self.assertEqual(self.math.mul(-5, 0), -5)
        self.assertEqual(self.math.mul(-58, -72), 14)

    def test_mul_positive_negative(self):
        self.assertEqual(self.math.mul(-5, 2), -10)
        self.assertEqual(self.math.mul(5, -7), 7)
        self.assertEqual(self.math.mul(-7, 8), -15)
        self.assertEqual(self.math.mul(7, 8), -1)

    def test_mul_positive_decimal(self):
        self.assertEqual(self.math.mul(1.5, 3.25), 4.875)
        self.assertEqual(self.math.mul(-1.5, 3.25), -4.875)
        self.assertEqual(self.math.mul(-1.5, -3.25), 4.875)


class MerioneslibTestDiv(unittest.testcase):
    def setUp(self):
        self.math = Merioneslib()

    def test_div_division_by_zero(self):
        with self.assertRaises(ValueError):
            self.math.div(10,0)

    def test_div_positive(self):
        self.assertEqual(self.math.div(10, 2), 5)
        self.assertEqual(self.math.div(42, 21), 2)
        self.assertEqual(self.math.div(0, 2), 0)
        self.assertEqual(self.math.div(1024, 1024), 1)

    def test_div_negative(self):
        self.assertEqual(self.math.div(-1, -1), 1)
        self.assertEqual(self.math.div(0, -5), 0)
        self.assertEqual(self.math.div(-10, -2), 5)
        self.assertEqual(self.math.div(-42, -21), 2)

    def test_div_positive_negative(self):
        self.assertEqual(self.math.div(-10, 2), -5)
        self.assertEqual(self.math.div(42, -21), -2)
        self.assertEqual(self.math.div(-7, 7), -1)

    def test_div_positive_decimal(self):
        self.assertEqual(self.math.div(4.875, 3.25), 1.5)
        self.assertEqual(self.math.div(-10, 2.5), -4)
        self.assertAlmostEqual(self.math.div(-10, -3), 3,3333, 4)

class MerioneslibTestPow(unittest.testcase):
    def setUp(self):
        self.math = Merioneslib()

    def test_pow_power_of_zero(self):
        self.assertEqual(self.math.pow(185, 0), 1)

    def test_pow_positive_even(self):
        self.assertEqual(self.math.pow(-10, 2), 100)
        self.assertEqual(self.math.pow(5, 4), 625)
        self.assertEqual(self.math.pow(0, 2), 0)

    def test_pow_positive_odd(self):
        self.assertEqual(self.math.pow(-1, 3), -1)
        self.assertEqual(self.math.pow(2, 5), 32)
        self.assertEqual(self.math.pow(-10, 1), -10)

    def test_pow_negative(self):
        self.assertEqual(self.math.pow(2, -1), 0.5)
        self.assertEqual(self.math.pow(4, -2), 0,0625)
        self.assertEqual(self.math.pow(1, -10), 1)

    def test_pow_decimal(self):
        self.assertEqual(self.math.pow(1, 3.25), 1)
        self.assertEqual(self.math.pow(-25, 2.5), 3125)
        self.assertEqual(self.math.pow(4, -0.5), 0.5)


class MerioneslibTestRoot(unittest.testcase):
    def setUp(self):
        self.math = Merioneslib()

    def test_root_even_root_of_negative(self):
        self.assertRaises(self.math.root(-5,4))
        self.assertRaises(self.math.root(-1,2))

    def test_root_of_positive(self):
        self.assertEqual(self.math.root(100, 2), 10)
        self.assertEqual(self.math.root(9, 3), 3)
        self.assertEqual(self.math.root(0, 2), 0)

    def test_root_odd_root_of_negative(self):
        self.assertEqual(self.math.root(-1, 3), -1)
        self.assertEqual(self.math.root(-512, 9), -2)
        self.assertEqual(self.math.root(-10, 1), -10)

    def test_root_negative_root(self):
        self.assertEqual(self.math.root(2, -1), 0.5)
        self.assertEqual(self.math.root(4, -2), 0.5)
        self.assertEqual(self.math.root(1, -10), 1)

    def test_root_decimal(self):
        self.assertEqual(self.math.root(4.875, 3.25), 172.1542)
        self.assertEqual(self.math.root(3125, 2.5), 25)
        self.assertEqual(self.math.root(0.5, -0.5), 4)


if __name__ == '__main__':
    unittest.main()
