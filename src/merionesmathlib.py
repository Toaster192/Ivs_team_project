##
# @package merioneslib
# Merioneslib is a mathematical library for Meriones calculator.
#
# This mathematical library consists of basic mathematical operations
# such as sum, difference, multiplication or division, advanced mathematical
# operations such as power, ..., logarithm,.... **DOPLNIT**
#


# @brief Class for Meriones Math Library
class MerionesLib:

    ##
    # @brief Sum of two numbers
    #
    # @param a First number to be added
    # @param b Second number to be added
    #
    # @return Sum of two numbers a and b

    @staticmethod
    def add(a, b):
        return a + b

    ##
    # @brief Difference of two numbers
    #
    # @param a First number, minor
    # @param b Second number, minority
    #
    # @return Difference of two numbers a and b

    @staticmethod
    def sub(a, b):
        return a - b

    ##
    # @brief Product of two numbers
    #
    # @param a First number to be multiplied
    # @param b Second number to be multiplied
    #
    # @return Product of two numbers a and b

    @staticmethod
    def mul(a, b):
        return a * b

    ##
    # @brief Quotient of two numbers
    #
    # @param a First number, dividend
    # @param b Second number, divisor
    #
    # @return Quotient of two numbers a and b
    # @exceptions Ma ERROR In case the second number is zero, function will throw error Ma ERROR

    @staticmethod
    def div(a, b):
        if not b:
            print("Error - division by zero!")
            raise ValueError('Ma ERROR')
        if a % b == 0:
            return a / b
        a = float(a)
        return a / b

    """ Alpha version, waiting for SolveEquation to be done
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
    """

    ##
    # Method computes factorial of n
    #
    # @param n number of which factorial is calculated
    # @return factorial of number n

    @staticmethod
    def factorial(n):
        if type(n) != int or n < 0:
            print("Error - wrong factorial number format!")
            raise ValueError('Ma ERROR')            
        if n == 0:
            return 1
        else:
            return n * MerionesLib.factorial(n-1)

    ##
    # Method calculates a base raised to a power
    #
    # @param base base of the power
    # @param exponent exponent determines how many times the base will be multiplied
    # @return base raised to the power

    @staticmethod
    def power(base, exponent):
        if type(exponent) != int or n <= 0:
            print("Error - exponent has to be integer!")
            raise ValueError('Ma ERROR')
        return base**exponent

    ##
    # Method calculates square root of n
    #
    # @param n number of which square root will be calculate
    # @return square root of n

    @staticmethod
    def root(n, rvalue):
        if type(exponent) != int or n == 0:
            print("Error - root value has to be integer!")
            raise ValueError('Ma ERROR')
        return n ** (1/rvalue)

    ##
    # Method calculates natural logarithm of x
    #
    # @param x number of which natural logarithm will be calculate
    # @return natural logarithm of x

    @staticmethod
    def ln(x):
        n = 100000000.0
        return n * ((x ** (1/n)) - 1)

    ##
    # Method converts number x to units given by parameter units
    #
    # @param x number of kilograms
    # @param units units that user requested
    # @return number x converted to given units

    @staticmethod
    def convert_weight(x, units):
        if units != 'mg' and units != 'g' and units != 'lb' and units != 't':
            print("Error - wrong units!")
            raise ValueError('Ma ERROR')
        if units == 'mg':
            return x * 1000 ** 2
        elif units == 'g':
            return x * 1000
        elif units == 'lb':
            return x * 2.20462262
        elif units == 't':
            return x * 0.001

    ##
    # Method converts number x to units given by parameter units
    #
    # @param x number of kilometers
    # @param units units that user requested
    # @return number x converted to given units

    @staticmethod
    def convert_length(x, units):
        if units != 'm' and units != 'cm' and units != 'mm' and units != 'mi':
            print("Error - wrong units!")
            raise ValueError('Ma ERROR')
        if units == 'm':
            return x * 1000
        elif units == 'cm':
            return x * 100000
        elif units == 'mm':
            return x * 1000**2
        elif units == 'mi':
            return x * 0.62137199

    ##
    # Method converts number x to units given by parameter units
    #
    # @param x number of hours
    # @param units units that user requested
    # @return number x converted to given units

    @staticmethod
    def convert_time(x, units):
        if units != 'min' and units != 's' and units != 'day':
            print("Error - wrong units!")
            raise ValueError('Ma ERROR')
        if units == 'min':
            return x * 60
        elif units == 's':
            return x * 3600
        elif units == 'day':
            return x * 0.0416667

    ##
    # Method converts number x to units given by parameter units
    #
    # @param x number of celsius
    # @param units units that user requested
    # @return number x converted to given units

    @staticmethod
    def convert_degrees(x, units):
        if units != 'K' and units != 'F':
            print("Error - wrong units!")
            raise ValueError('Ma ERROR')
        if units == 'K':
            return x + 273.15
        elif units == 'F':
            return (x * 9/5) + 32
