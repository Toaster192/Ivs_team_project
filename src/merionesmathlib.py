## @package merioneslib
#  Merioneslib is a mathematical library for Meriones calculator.
#
#  More details...

##
# @brief Sum of two numbers
#
# @param a First number to be added
# @param b Second number to be added
#
# @return Sum of two numbers a and b
def Add(a,b):
    return a + b

##
# @brief Difference of two numbers
#
# @param a First number, minor
# @param b Second number, minority
#
# @return Difference of two numbers a and b
def Sub(a,b):
    return a - b

##
# @brief Product of two numbers
#
# @param a First number to be multiplied
# @param b Second number to be multiplied
#
# @return Product of two numbers a and b
def Mul(a,b):
    return a * b

##
# @brief Quotient of two numbers
#
# @param a First number, dividend
# @param b Second number, divisor
#
# @return Quotient of two numbers a and b or "Ma ERROR" in case
# the first number is divided by zero
def Div(a,b):
    if(b == 0):
        print("Error - division by zero!")
        raise ValueError('Ma ERROR')
    return a / b
