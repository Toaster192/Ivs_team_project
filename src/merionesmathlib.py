##
# @package merioneslib
#  Merioneslib is a mathematical library for Meriones calculator.
#
#  This mathematical library consists of basic mathematical operations
#  such as sum, difference, multiplication or division, advanced mathematical
#  operations such as power, ..., logarithm,.... **DOPLNIT**

from src.extraFunctions import *
from src.mandatoryFunctions import *

##
# @brief Class for Meriones Math Library
class MerionesLib:


##
# @brief Sum of two numbers
#
# @param a First number to be added
# @param b Second number to be added
#
# @return Sum of two numbers a and b
    def add(self, a, b):
        return a + b


##
# @brief Difference of two numbers
#
# @param a First number, minor
# @param b Second number, minority
#
# @return Difference of two numbers a and b
    def sub(self, a, b):
        return a - b


##
# @brief Product of two numbers
#
# @param a First number to be multiplied
# @param b Second number to be multiplied
#
# @return Product of two numbers a and b
    def mul(self, a, b):
        return a * b


##
# @brief Quotient of two numbers
#
# @param a First number, dividend
# @param b Second number, divisor
#
# @return Quotient of two numbers a and b 
# @exceptions Ma ERROR In case the second number is zero, function will throw error Ma ERROR
    def div(self, a, b):
        if not b:
            print("Error - division by zero!")
            raise ValueError('Ma ERROR')
        if a % b == 0:
	        return a / b
        a = float(a)
        return a / b


''' Alpha version
def ParetheParse(str_input, remains):
    str_input.strip()
    braces = {'(': ')'}     # Could add '[': ']', '{': '}' etc.
    for i, c in enumerate(str_input):
        if c in braces.keys():
            remains.append(i)
            remains.append(braces.get(c))
        if c in remains[-1]:
            if remains.len() < 2:
                print("Parentheses error (too many ending parentheses)")
                raise ValueError('Ma ERROR')
            remains.pop()
            j = remains[-1]
            remains.pop()
            temp = ParetheParse(str_input[j:i], remains)
            str_input = str_input[:j] + temp + str_input[i:]
    if remains:
        print("Parentheses error (too many beginning parentheses)")
        raise ValueError('Ma ERROR')
    return SolveEquation(str_input)
'''
