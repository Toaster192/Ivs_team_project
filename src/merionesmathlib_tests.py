# MerionesLib_tests.py
# Projekt IVS II.
# Autor: Jaromír Wysoglad, xwysog00
# Datum: 2018-03-26

import unittest

from src.merionesmathlib import MerionesLib


# To run tests, go to the parent directory and
# type "python3 -m tests.merioneslib_tests"

# Tests the add function (+)
class MerionesLibTestAdd(unittest.TestCase):
    def setUp(self):
        self.math = MerionesLib()

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


# Tests the sub function (-)
class MerionesLibTestSub(unittest.TestCase):
    def setUp(self):
        self.math = MerionesLib()

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


# Tests the mul function (*)
class MerionesLibTestMul(unittest.TestCase):
    def setUp(self):
        self.math = MerionesLib()

    def test_mul_positive(self):
        self.assertEqual(self.math.mul(1, 2), 2)
        self.assertEqual(self.math.mul(0, 0), 0)
        self.assertEqual(self.math.mul(0, 2), 0)
        self.assertEqual(self.math.mul(72, 58), 4176)

    def test_mul_negative(self):
        self.assertEqual(self.math.mul(-1, -1), 1)
        self.assertEqual(self.math.mul(0, -5), 0)
        self.assertEqual(self.math.mul(-5, 0), 0)
        self.assertEqual(self.math.mul(-58, -72), 4176)

    def test_mul_positive_negative(self):
        self.assertEqual(self.math.mul(-5, 2), -10)
        self.assertEqual(self.math.mul(5, -7), -35)
        self.assertEqual(self.math.mul(-7, 8), -56)
        self.assertEqual(self.math.mul(7, 8), 56)

    def test_mul_positive_decimal(self):
        self.assertEqual(self.math.mul(1.5, 3.25), 4.875)
        self.assertEqual(self.math.mul(-1.5, 3.25), -4.875)
        self.assertEqual(self.math.mul(-1.5, -3.25), 4.875)


# Tests the div function (/)
class MerionesLibTestDiv(unittest.TestCase):
    def setUp(self):
        self.math = MerionesLib()

    # Division by zero is usually forbidden in math
    def test_div_division_by_zero(self):
        with self.assertRaises(ValueError):
            self.math.div(10, 0)

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

    def test_div_decimal(self):
        self.assertEqual(self.math.div(4.875, 3.25), 1.5)
        self.assertEqual(self.math.div(-10, 2.5), -4)
        self.assertAlmostEqual(self.math.div(-10, -3), 3.3333, 4)


# Tests the power function (^)
class MerionesLibTestPower(unittest.TestCase):
    def setUp(self):
        self.math = MerionesLib()

    def test_power_positive_even(self):
        self.assertEqual(self.math.power(-10, 2), 100)
        self.assertEqual(self.math.power(5, 4), 625)
        self.assertEqual(self.math.power(0, 2), 0)

    def test_power_positive_odd(self):
        self.assertEqual(self.math.power(-1, 3), -1)
        self.assertEqual(self.math.power(2, 5), 32)
        self.assertEqual(self.math.power(-10, 1), -10)

    # It is required by the assignment that power can have only natural number as an exponent
    def test_power_forbidden_exponents(self):
        with self.assertRaises(ValueError):
            self.math.power(185, 0)
        with self.assertRaises(ValueError):
            self.math.power(2, -1)
        with self.assertRaises(ValueError):
            self.math.power(1, -10)
        with self.assertRaises(ValueError):
            self.math.power(-25, 2.5)
        with self.assertRaises(ValueError):
            self.math.power(4, -0.5)


# Tests the root function (√)
class MerionesLibTestRoot(unittest.TestCase):
    def setUp(self):
        self.math = MerionesLib()

    # Even root of negative number is usually forbidden in math
    def test_root_even_root_of_negative(self):
        with self.assertRaises(ValueError):
            self.math.root(-4, 4)

        with self.assertRaises(ValueError):
            self.math.root(-10, 2)

    def test_root_of_positive(self):
        self.assertEqual(self.math.root(100, 2), 10)
        self.assertEqual(self.math.root(27, 3), 3)
        self.assertEqual(self.math.root(0, 2), 0)

    def test_root_odd_root_of_negative(self):
        with self.assertRaises(ValueError):
            self.math.root(-1, 3)
        with self.assertRaises(ValueError):
            self.math.root(-512, 9)
        with self.assertRaises(ValueError):
            self.math.root(-10, 1)

    def test_root_negative_root(self):
        with self.assertRaises(ValueError):
            self.math.root(2, -1)
        with self.assertRaises(ValueError):
            self.math.root(4, -2)
        with self.assertRaises(ValueError):
            self.math.root(1, -10)

    def test_root_decimal(self):
        self.assertAlmostEqual(self.math.root(172.1542, 3.25), 4.875, 4)
        self.assertEqual(self.math.root(3125, 2.5), 25)
        self.assertEqual(self.math.root(0.5, 0.5), 0.25)


# Tests the factorial function (!)
class MerionesLibTestFactorial(unittest.TestCase):
    def setUp(self):
        self.math = MerionesLib()

    # Factorial of negative number is forbidden in math
    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            self.math.factorial(-5)
        with self.assertRaises(ValueError):
            self.math.factorial(-1)

    # Factorial of decimal number is usually forbidden in math
    def test_factorial_decimal(self):
        with self.assertRaises(ValueError):
            self.math.factorial(1.5)
        with self.assertRaises(ValueError):
            self.math.factorial(-2.89)

    # Factorial of zero is 1 by definition
    def test_factorial_of_zero(self):
        self.assertEqual(self.math.factorial(0), 1)

    def test_factorial_of_positive(self):
        self.assertEqual(self.math.factorial(1), 1)
        self.assertEqual(self.math.factorial(5), 120)
        self.assertEqual(self.math.factorial(10), 3628800)


# Tests the natural logarithm function (ln)
class MerionesLibTestLn(unittest.TestCase):
    def setUp(self):
        self.math = MerionesLib()

    # Natural logarithm of negative number and zero is forbidden in math
    def test_ln_negative_zero(self):
        with self.assertRaises(ValueError):
            self.math.ln(-5)
        with self.assertRaises(ValueError):
            self.math.ln(0)

    # Natural logarithm of one is zero
    def test_ln_one(self):
        self.assertEqual(self.math.ln(1), 0)

    def test_ln_of_positive(self):
        self.assertAlmostEqual(self.math.ln(0.5), -0.693147, 6)
        self.assertAlmostEqual(self.math.ln(2), 0.693147, 6)
        self.assertAlmostEqual(self.math.ln(0.1), -2.302585, 6)
        self.assertAlmostEqual(self.math.ln(10), 2.302585, 6)


# Tests the solve_expression function
class MerionesLibTestSolveExpression(unittest.TestCase):
    def setUp(self):
        self.math = MerionesLib()

    def test_solve_expression_addition(self):
        self.assertEqual(self.math.solve_expression("5+8"), 13)
        self.assertEqual(self.math.solve_expression("-10+19"), 9)
        self.assertEqual(self.math.solve_expression("5+-9"), -4)
        self.assertEqual(self.math.solve_expression("4.5+10"), 14.5)
        self.assertEqual(self.math.solve_expression("9+-4.5"), 4.5)

    def test_solve_expression_subtraction(self):
        self.assertEqual(self.math.solve_expression("5-8"), -3)
        self.assertEqual(self.math.solve_expression("-10-19"), -29)
        self.assertEqual(self.math.solve_expression("5--9"), 14)
        self.assertEqual(self.math.solve_expression("4.5-10"), -5.5)
        self.assertEqual(self.math.solve_expression("9-4.5"), 4.5)

    def test_solve_expression_multiplication(self):
        self.assertEqual(self.math.solve_expression("5*8"), 40)
        self.assertEqual(self.math.solve_expression("-10*19"), -190)
        self.assertEqual(self.math.solve_expression("5*-9"), -45)
        self.assertEqual(self.math.solve_expression("4.5*10"), 45)
        self.assertEqual(self.math.solve_expression("9*-4.5"), -40.5)

    def test_solve_expression_division(self):
        self.assertEqual(self.math.solve_expression("5/8"), 0.625)
        self.assertEqual(self.math.solve_expression("-10/5"), -2)
        self.assertEqual(self.math.solve_expression("5/-25"), -0.2)
        self.assertEqual(self.math.solve_expression("4.5/10"), 0.45)
        self.assertEqual(self.math.solve_expression("9/-4.5"), -2)

        # Division by zero is forbidden in math
        with self.assertRaises(ValueError):
            self.math.solve_expression("-5/0")

    def test_solve_expression_power(self):
        self.assertEqual(self.math.solve_expression("5^8"), 390625)
        self.assertEqual(self.math.solve_expression("-10^5"), -100000)
        self.assertEqual(self.math.solve_expression("-10^4"), 10000)
        self.assertEqual(self.math.solve_expression("4.5^5"), 1845.28125)

    def test_solve_expression_root(self):
        self.assertEqual(self.math.solve_expression("3√8"), 2)
        self.assertEqual(self.math.solve_expression("√16"), 4)
        self.assertEqual(self.math.solve_expression("3√125"), 5)
        self.assertEqual(self.math.solve_expression("5√100000"), 10)
        self.assertEqual(self.math.solve_expression("3√12.167"), 2.3)

        # Even root of negative number is forbidden in math
        with self.assertRaises(ValueError):
            self.math.solve_expression("4√-2")
        with self.assertRaises(ValueError):
            self.math.solve_expression("√-2")

    def test_solve_expression_factorial(self):
        self.assertEqual(self.math.solve_expression("0!"), 1)
        self.assertEqual(self.math.solve_expression("1!"), 1)
        self.assertEqual(self.math.solve_expression("2!"), 2)
        self.assertEqual(self.math.solve_expression("5!"), 120)

        # Factorials of negative nad decimal numbers are forbidden in math
        with self.assertRaises(ValueError):
            self.math.solve_expression("0.5!")
        with self.assertRaises(ValueError):
            self.math.solve_expression("-1!")

    def test_solve_expression_ln(self):
        self.assertEqual(self.math.solve_expression("ln1"), 0)
        self.assertAlmostEqual(self.math.solve_expression("ln0.2"), -1.6094379, 7)
        self.assertAlmostEqual(self.math.solve_expression("ln2"), 0.693147, 6)
        self.assertAlmostEqual(self.math.solve_expression("ln0.2"), -1.6094379, 7)

        # Natural logarithm of negative number or zero is forbidden in math
        with self.assertRaises(ValueError):
            self.math.solve_expression("ln0")
        with self.assertRaises(ValueError):
            self.math.solve_expression("ln-42")

    def test_solve_expression_multiple_operations(self):
        self.assertEqual(self.math.solve_expression("5+8/2*10"), 45)
        self.assertEqual(self.math.solve_expression("5^2+10*2"), 45)
        self.assertEqual(self.math.solve_expression("2!*8+1"), 17)
        self.assertEqual(self.math.solve_expression("1*5/5+1-1*3/3^1"), 1)

        with self.assertRaises(ValueError):
            self.math.solve_expression("2!*8+1/0")
        with self.assertRaises(ValueError):
            self.math.solve_expression("2!*8+1--1!")
        with self.assertRaises(ValueError):
            self.math.solve_expression("2!*8+1-ln0")


# Tests the parse_parentheses function
class MerionesLibTestParseParentheses(unittest.TestCase):
    def setUp(self):
        self.math = MerionesLib()

    def test_parse_parentheses(self):
        self.assertEqual(self.math.parse_parentheses("(5+8)*2"), "26")
        self.assertEqual(self.math.parse_parentheses("-(10+19)"), "-29")
        self.assertEqual(self.math.parse_parentheses("(1+2)!"), "6")
        self.assertEqual(self.math.parse_parentheses("((1+2)*(1-2))*3"), "-9")
        self.assertEqual(self.math.parse_parentheses("(((((9+1))))/2)^(((1+2)*2)/2)"), "125")
        self.assertEqual(self.math.parse_parentheses("ln(1)"), "0")

    def test_parse_parentheses_forbidden_expressions(self):
        with self.assertRaises(ValueError):
            self.math.solve_expression("(1-2)!")
        with self.assertRaises(ValueError):
            self.math.solve_expression("ln(125*0)")
        with self.assertRaises(ValueError):
            self.math.solve_expression("(1+3)√(2*(3-4))")

    # incomplete parentheses (different count of opening and closing parentheses) are forbidden
    def test_parse_parentheses_incomplete_parentheses(self):
        with self.assertRaises(ValueError):
            self.math.solve_expression("(1+5")
        with self.assertRaises(ValueError):
            self.math.solve_expression("1+5)")
        with self.assertRaises(ValueError):
            self.math.solve_expression("(2+5)*(1-8)/)+8-(2!)")


# Tests the convert_weight function
class MerionesLibTestConvertWeight(unittest.TestCase):
    def setUp(self):
        self.math = MerionesLib()

    def test_convert_to_mg(self):
        self.assertEqual(self.math.convert_weight(10, "mg"), 10000000)
        self.assertEqual(self.math.convert_weight(0, "mg"), 0)
        self.assertEqual(self.math.convert_weight(2.5, "mg"), 2500000)

    def test_convert_to_g(self):
        self.assertEqual(self.math.convert_weight(10, "g"), 10000)
        self.assertEqual(self.math.convert_weight(0, "g"), 0)
        self.assertEqual(self.math.convert_weight(2.5, "g"), 2500)

    def test_convert_to_lb(self):
        self.assertAlmostEqual(self.math.convert_weight(10, "lb"), 22.0462, 4)
        self.assertEqual(self.math.convert_weight(0, "lb"), 0)
        self.assertAlmostEqual(self.math.convert_weight(2.5, "lb"), 5.5116, 4)

    def test_convert_to_t(self):
        self.assertEqual(self.math.convert_weight(10, "t"), 0.01)
        self.assertEqual(self.math.convert_weight(0, "t"), 0)
        self.assertEqual(self.math.convert_weight(2.5, "t"), 0.0025)
        
    def test_convert_mg_to_other(self):
        self.assertEqual(self.math.convert_weight(100, "kg", "mg"), 0.0001)
        self.assertEqual(self.math.convert_weight(100, "mg", "mg"), 100)
        self.assertEqual(self.math.convert_weight(100, "g", "mg"), 0.1)
        self.assertEqual(self.math.convert_weight(100, "lb", "mg"), 0.000220462262)
        self.assertEqual(self.math.convert_weight(100, "t", "mg"), 0.0000001)
    
    def test_convert_g_to_other(self):
        self.assertEqual(self.math.convert_weight(100, "kg", "g"), 0.1)
        self.assertEqual(self.math.convert_weight(100, "mg", "g"), 100000)
        self.assertEqual(self.math.convert_weight(100, "g", "g"), 100)
        self.assertEqual(self.math.convert_weight(100, "lb", "g"), 0.220462262)
        self.assertEqual(self.math.convert_weight(100, "t", "g"), 0.0001)
        
    def test_convert_lb_to_other(self):
        self.assertEqual(self.math.convert_weight(100, "kg", "lb"), 45.359237)
        self.assertEqual(self.math.convert_weight(100, "mg", "lb"), 45359237)
        self.assertEqual(self.math.convert_weight(100, "g", "lb"), 45359.237)
        self.assertEqual(self.math.convert_weight(100, "lb", "lb"), 100)
        self.assertEqual(self.math.convert_weight(100, "t", "lb"), 0.045359237)
    
    def test_convert_t_to_other(self):
        self.assertEqual(self.math.convert_weight(100, "kg", "t"), 100000)
        self.assertEqual(self.math.convert_weight(100, "mg", "t"), 100000000000)
        self.assertEqual(self.math.convert_weight(100, "g", "t"), 100000000)
        self.assertEqual(self.math.convert_weight(100, "lb", "t"), 220462.262)
        self.assertEqual(self.math.convert_weight(100, "t", "t"), 100)
            

# Tests the convert_length function
class MerionesLibTestConvertLength(unittest.TestCase):
    def setUp(self):
        self.math = MerionesLib()

    def test_convert_to_m(self):
        self.assertEqual(self.math.convert_length(10, "m"), 10000)
        self.assertEqual(self.math.convert_length(0, "m"), 0)
        self.assertEqual(self.math.convert_length(2.5, "m"), 2500)

    def test_convert_to_cm(self):
        self.assertEqual(self.math.convert_length(10, "cm"), 1000000)
        self.assertEqual(self.math.convert_length(0, "cm"), 0)
        self.assertEqual(self.math.convert_length(2.5, "cm"), 250000)

    def test_convert_to_mi(self):
        self.assertAlmostEqual(self.math.convert_length(10, "mi"), 6.2137, 4)
        self.assertEqual(self.math.convert_length(0, "mi"), 0)
        self.assertAlmostEqual(self.math.convert_length(2.5, "mi"), 1.5534, 4)

    def test_convert_to_mm(self):
        self.assertEqual(self.math.convert_length(10, "mm"), 10000000)
        self.assertEqual(self.math.convert_length(0, "mm"), 0)
        self.assertEqual(self.math.convert_length(2.5, "mm"), 2500000)
        
    def test_convert_m_to_other(self):
        self.assertEqual(self.math.convert_length(100, "km", "m"), 0.1)
        self.assertEqual(self.math.convert_length(100, "m", "m"), 100)
        self.assertEqual(self.math.convert_length(100, "cm", "m"), 10000)
        self.assertEqual(self.math.convert_length(100, "mi", "m"), 0.0621371192)
        self.assertEqual(self.math.convert_length(100, "mm", "m"), 100000)
    
    def test_convert_cm_to_other(self):
        self.assertEqual(self.math.convert_length(100, "km", "cm"), 0.001)
        self.assertEqual(self.math.convert_length(100, "m", "cm"), 1)
        self.assertEqual(self.math.convert_length(100, "cm", "cm"), 100)
        self.assertEqual(self.math.convert_length(100, "mi", "cm"), 0.000621371192)
        self.assertEqual(self.math.convert_length(100, "mm", "cm"), 1000)
    
    def test_convert_mi_to_other(self):
        self.assertEqual(self.math.convert_length(100, "km", "mi"), 160.9344)
        self.assertEqual(self.math.convert_length(100, "m", "mi"), 160934.4)
        self.assertEqual(self.math.convert_length(100, "cm", "mi"), 16093440)
        self.assertEqual(self.math.convert_length(100, "mi", "mi"), 100)
        self.assertEqual(self.math.convert_length(100, "mm", "mi"), 160934400)
    
    def test_convert_mm_to_other(self):
        self.assertEqual(self.math.convert_length(100, "km", "mm"), 0.0001)
        self.assertEqual(self.math.convert_length(100, "m", "mm"), 0.1)
        self.assertEqual(self.math.convert_length(100, "cm", "mm"), 10)
        self.assertEqual(self.math.convert_length(100, "mi", "mm"), 0.0000621371192)
        self.assertEqual(self.math.convert_length(100, "mm", "mm"), 100)


# Tests the convert_time function
class MerionesLibTestConvertTime(unittest.TestCase):
    def setUp(self):
        self.math = MerionesLib()

    def test_convert_to_min(self):
        self.assertEqual(self.math.convert_time(10, "min"), 600)
        self.assertEqual(self.math.convert_time(0, "min"), 0)
        self.assertEqual(self.math.convert_time(2.512, "min"), 150.72)

    def test_convert_to_s(self):
        self.assertEqual(self.math.convert_time(10, "s"), 36000)
        self.assertEqual(self.math.convert_time(0, "s"), 0)
        self.assertEqual(self.math.convert_time(2.512, "s"), 9043.2)

    def test_convert_to_day(self):
        self.assertAlmostEqual(self.math.convert_time(8, "day"), 0.3333, 4)
        self.assertEqual(self.math.convert_time(0, "day"), 0)
        self.assertEqual(self.math.convert_time(24, "day"), 1)
        self.assertAlmostEqual(self.math.convert_time(245, "day"), 10.2083, 4)
        
    def test_convert_day_to_other(self):
        self.assertEqual(self.math.convert_time(100, "day", "day"), 100)
        self.assertEqual(self.math.convert_time(100, "h", "day"), 2400)
        self.assertEqual(self.math.convert_time(100, "min", "day"), 144000)
        self.assertEqual(self.math.convert_time(100, "s", "day"), 8640000)
    
    def test_convert_min_to_other(self):
        self.assertEqual(self.math.convert_time(100, "day", "min"), 0.0694444444444)
        self.assertEqual(self.math.convert_time(100, "h", "min"), 1.6666666666667)
        self.assertEqual(self.math.convert_time(100, "min", "min"), 100)
        self.assertEqual(self.math.convert_time(100, "s", "min"), 6000)
        
    def test_convert_s_to_other(self):
        self.assertEqual(self.math.convert_time(100, "day", "s"), 0.0011574074074)
        self.assertEqual(self.math.convert_time(100, "h", "s"), 0.0277777777778)
        self.assertEqual(self.math.convert_time(100, "min", "s"), 1.6666666666667)
        self.assertEqual(self.math.convert_time(100, "s", "s"), 100)



# Tests the convert_degrees function
class MerionesLibTestConvertDegrees(unittest.TestCase):
    def setUp(self):
        self.math = MerionesLib()

    def test_convert_to_k(self):
        self.assertEqual(self.math.convert_degrees(10, "K"), 283.15)
        self.assertEqual(self.math.convert_degrees(0, "K"), 273.15)
        self.assertEqual(self.math.convert_degrees(250, "K"), 523.15)
        self.assertEqual(self.math.convert_degrees(-50, "K"), 223.15)

    def test_convert_to_f(self):
        self.assertEqual(self.math.convert_degrees(10, "°F"), 50)
        self.assertEqual(self.math.convert_degrees(0, "°F"), 32)
        self.assertEqual(self.math.convert_degrees(250, "°F"), 482)
        self.assertEqual(self.math.convert_degrees(-50, "°F"), -58)


# Tests the parse_expression function
class MerionesLibTestParseExpression(unittest.TestCase):
    def setUp(self):
        self.math = MerionesLib()
        self.operators = ["ln", "!", "√", "^", "*", "/", "+", "-"]

    def test_parse_expression_unary_operation(self):
        self.assertEqual(self.math.parse_expression("3!", self.operators), ["3", "!"])
        self.assertEqual(self.math.parse_expression("-5", self.operators), ["-5"])
        self.assertEqual(self.math.parse_expression("ln0.3", self.operators), ["ln", "0.3"])
        self.assertEqual(self.math.parse_expression("√2", self.operators), ["√", "2"])

    def test_parse_expression_binary_operation(self):
        self.assertEqual(self.math.parse_expression("3+5", self.operators), ["3", "+", "5"])
        self.assertEqual(self.math.parse_expression("3.2*8.5", self.operators), ["3.2", "*", "8.5"])
        self.assertEqual(self.math.parse_expression("2-9", self.operators), ["2", "-", "9"])
        self.assertEqual(self.math.parse_expression("5/8", self.operators), ["5", "/", "8"])
        self.assertEqual(self.math.parse_expression("5--8", self.operators), ["5", "-", "-8"])
        self.assertEqual(self.math.parse_expression("5+-8", self.operators), ["5", "+", "-8"])
        self.assertEqual(self.math.parse_expression("5√8", self.operators), ["5", "√", "8"])
        self.assertEqual(self.math.parse_expression("5^8", self.operators), ["5", "^", "8"])

    def test_parse_expression_multiple_operations(self):
        self.assertEqual(self.math.parse_expression("3!+8/1*5", self.operators),
                         ["3", "!", "+", "8", "/", "1", "*", "5"])

        self.assertEqual(self.math.parse_expression("1*-5+8/3.5", self.operators),
                         ["1", "*", "-5", "+", "8", "/", "3.5"])

        self.assertEqual(self.math.parse_expression("ln-0.3+9^7", self.operators),
                         ["ln", "-0.3", "+", "9", "^", "7"])

    def test_parse_expression_e_number_notation(self):
        self.assertEqual(self.math.parse_expression("123e+123", self.operators), ["123e+123"])
        self.assertEqual(self.math.parse_expression("123e-123", self.operators), ["123e-123"])
        self.assertEqual(self.math.parse_expression("-123e+123--123e+123--123e+123",
                                                    self.operators), ["-123e+123", "-", "-123e+123", "-", "-123e+123"])

    # Tests for an raised exception when given a wrong expresion (multiple operators after each other,
    # unknown operators, ...)
    def test_parse_expression_wrong_expressions(self):
        with self.assertRaises(ValueError):
            self.math.parse_expression("+5", self.operators)
        with self.assertRaises(ValueError):
            self.math.parse_expression("5+", self.operators)
        with self.assertRaises(ValueError):
            self.math.parse_expression("--5", self.operators)
        with self.assertRaises(ValueError):
            self.math.parse_expression("1ln5", self.operators)
        with self.assertRaises(ValueError):
            self.math.parse_expression("3!5", self.operators)
        with self.assertRaises(ValueError):
            self.math.parse_expression("5+1++8", self.operators)
        with self.assertRaises(ValueError):
            self.math.parse_expression("+5-8", self.operators)
        with self.assertRaises(ValueError):
            self.math.parse_expression("5√", self.operators)


# Tests the str_to_num function
class MerionesLibTestStrToNum(unittest.TestCase):
    def setUp(self):
        self.math = MerionesLib()

    def test_str_to_num_ints(self):
        self.assertEqual(self.math.str_to_num("10"), 10)
        self.assertEqual(self.math.str_to_num("-0.0"), 0)
        self.assertEqual(self.math.str_to_num("-558"), -558)
        self.assertEqual(self.math.str_to_num("11.0"), 11)

    def test_str_to_num_floats(self):
        self.assertEqual(self.math.str_to_num("5.8"), 5.8)
        self.assertEqual(self.math.str_to_num("-0.8456"), -0.8456)
        self.assertEqual(self.math.str_to_num("7864.753"), 7864.753)

    def test_str_to_num_not_numbers(self):
        with self.assertRaises(ValueError):
            self.math.str_to_num("a")
        with self.assertRaises(ValueError):
            self.math.str_to_num("2.2.2.2")
        with self.assertRaises(ValueError):
            self.math.str_to_num("658+887.1")


if __name__ == '__main__':
    unittest.main()
