# merioneslib_tests.py
# Projekt IVS II.
# Autor: Jaromír Wysoglad, xwysog00
# Datum: 2018-03-26

import unittest

from src.merioneslib import Merioneslib


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
        self.assertEqual(self.math.sub(5, -7), 7)
        self.assertEqual(self.math.sub(-7, 8), -15)
        self.assertEqual(self.math.sub(7, 8), -1)

    def test_sub_decimal(self):
        self.assertEqual(self.math.sub(2.25, 4.5), -2.25)
        self.assertEqual(self.math.sub(-2.25, 4.5), -6.75)
        self.assertEqual(self.math.sub(-2.25, -4.5), 2.25)
