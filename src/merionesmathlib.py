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

    ##
    # Method recursively solves expressions in parentheses
    #
    # @param str_input The string input to be calculated
    # @param remains A list of unclosed braces (for recursion purposes, has default value)
    # @return The value of the input calculated in proper order

    @staticmethod
    def parse_parentheses(str_input, remains=None):
        if remains is None:
            remains = []

        str_input.strip()
        braces = {'(': ')'}     # Could add '[': ']', '{': '}' etc.
        for i, c in enumerate(str_input):
            if c in braces.keys():
                remains.append(i)
                remains.append(braces.get(c))

            if c in remains[-1]:
                if len(remains) < 2:
                    print("Parentheses error (too many ending parentheses)")
                    raise ValueError('Ma ERROR')

                remains.pop()
                j = remains[-1]
                remains.pop()
                temp = MerionesLib.parse_parentheses(str_input[j:i], remains)
                str_input = str_input[:j] + temp + str_input[i:]

        if remains:
            print("Parentheses error (too many beginning parentheses)")
            raise ValueError('Ma ERROR')

        return MerionesLib.solve_expression(str_input)

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
        if type(exponent) != int or exponent <= 0:
            print("Error - exponent has to be a positive integer!")
            raise ValueError('Ma ERROR')
        return base**exponent

    ##
    # Method calculates square root of n
    #
    # @param n number of which square root will be calculate
    # @return square root of n

    @staticmethod
    def root(n, rvalue):
        if type(rvalue) != int or (rvalue <= 0 and rvalue % 2 == 0):
            print("Error - root value has to be a positive or even, negative integer!")
            raise ValueError('Ma ERROR')
        return n ** (1/rvalue)

    ##
    # Method calculates natural logarithm of x
    #
    # @param x number of which natural logarithm will be calculate
    # @return natural logarithm of x

    @staticmethod
    def ln(x):
        if x <= 0:
            print("Error - ln value has to be more than 0!")
            raise ValueError('Ma ERROR')
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
        if units == 'mg':
            return x * 1000 ** 2
        elif units == 'g':
            return x * 1000
        elif units == 'lb':
            return x * 2.20462262
        elif units == 't':
            return x * 0.001
        else:
            print("Error - wrong units!")
            raise ValueError('Ma ERROR')

    ##
    # Method converts number x to units given by parameter units
    #
    # @param x number of kilometers
    # @param units units that user requested
    # @return number x converted to given units

    @staticmethod
    def convert_length(x, units):
        if units == 'm':
            return x * 1000
        elif units == 'cm':
            return x * 100000
        elif units == 'mm':
            return x * 1000**2
        elif units == 'mi':
            return x * 0.62137199
        else:
            print("Error - wrong units!")
            raise ValueError('Ma ERROR')

    ##
    # Method converts number x to units given by parameter units
    #
    # @param x number of hours
    # @param units units that user requested
    # @return number x converted to given units

    @staticmethod
    def convert_time(x, units):
        if units == 'min':
            return x * 60
        elif units == 's':
            return x * 3600
        elif units == 'day':
            return x * 0.0416667
        else:
            print("Error - wrong units!")
            raise ValueError('Ma ERROR')

    ##
    # Method converts number x to units given by parameter units
    #
    # @param x number of celsius
    # @param units units that user requested
    # @return number x converted to given units

    @staticmethod
    def convert_degrees(x, units):
        if units == 'K':
            return x + 273.15
        elif units == 'F':
            return (x * 9/5) + 32
        else:
            print("Error - wrong units!")
            raise ValueError('Ma ERROR')

    ##
    # Method divides expression to individual numbers and operators and saves that to a list
    #
    # @param expr mathematical expression to parse
    # @param operators operators that are used in given expression
    # @exception "Syn error" if there are syntactic errors in the expression (according to math)
    # @return expression converted to list of individual numbers and operators

    @staticmethod
    def parse_expression(expr, operators):
        result = [expr]

        for operator in operators:
            expression = []
            expression.extend(result)

            for m in expression:
                if operator in m:
                    new_expression = m.split(operator)
                    i = 1

                    while i < len(new_expression):
                        new_expression.insert(i, operator)
                        i += 2
                    new_expression = (filter(lambda a: a != "", new_expression))

                    index = result.index(m)
                    result.remove(m)

                    for n in new_expression:
                        result.insert(index, n)
                        index += 1

        for index, item in enumerate(result):
            if item == "-" and (index == 0 or result[index - 1] in operators):
                result[index:index + 2] = [''.join(result[index:index + 2])]

        # check the parsed expression for syntactic errors
        for index, item in enumerate(result):
            # check for operators on the begining or end of expression
            if item in operators:
                if index == 0 and item != "ln" and item != "√":
                    raise ValueError("Syn Error")
                if index == len(result) - 1 and item != "!":
                    raise ValueError("Syn Error")

            # check for forbidden double operators
            if item in operators and result[index - 1] in operators:
                if index > 0 and result[index - 1] != "!" and item != "ln" and item != "√":
                    raise ValueError("Syn Error")

            # check if there is an operator after ! and before ln
            if item == "!" and index < len(result) - 1 and result[index + 1] not in operators:
                raise ValueError("Syn Error")

            if item == "ln" and index > 0 and result[index - 1] not in operators:
                raise ValueError("Syn Error")

            if item not in operators:
                # check if it is a valid number
                float(item)

        return result

    ##
    # Method converts string either to int or float depending on its value
    #
    # @param s string containing correct number
    # @exception when the given string isn't a number
    # @return converted number (int or float)

    @staticmethod
    def str_to_num(s):
        number = s.split(".")
        if len(number) == 1 or int(number[1]) == 0:
            return int(number[0])
        else:
            return float(s)

    ##
    # Method solves mathematical expressions without parentheses
    #
    # @param expr mathematical expression as a string
    # @exception when there is either a syntactic or mathematical error in the expression
    # @return value of the expression (one number)

    @staticmethod
    def solve_expression(expr):
        operators = ["ln", "!", "√", "^", "*", "/", "+", "-"]
        expression = MerionesLib.parse_expression(expr, operators)

        operator_precedence = [["ln"], ["!"], ["^", "√"], ["*", "/"], ["+", "-"]]
        for operator in operator_precedence:
            index = 0
            while index < len(expression):
                item = expression[index]
                if item in operator:
                    if item == "+":
                        result = [str(MerionesLib.add(MerionesLib.str_to_num(expression[index - 1]),
                                                      MerionesLib.str_to_num(expression[index + 1])))]
                        expression[index - 1:index + 2] = result
                        index -= 1

                    elif item == "-":
                        result = [str(MerionesLib.sub(MerionesLib.str_to_num(expression[index - 1]),
                                                      MerionesLib.str_to_num(expression[index + 1])))]
                        expression[index - 1:index + 2] = result
                        index -= 1

                    elif item == "*":
                        result = [str(MerionesLib.mul(MerionesLib.str_to_num(expression[index - 1]),
                                                      MerionesLib.str_to_num(expression[index + 1])))]
                        expression[index - 1:index + 2] = result
                        index -= 1

                    elif item == "/":
                        result = [str(MerionesLib.div(MerionesLib.str_to_num(expression[index - 1]),
                                                      MerionesLib.str_to_num(expression[index + 1])))]
                        expression[index - 1:index + 2] = result
                        index -= 1

                    elif item == "^":
                        result = [str(MerionesLib.power(MerionesLib.str_to_num(expression[index - 1]),
                                                        MerionesLib.str_to_num(expression[index + 1])))]
                        expression[index - 1:index + 2] = result
                        index -= 1

                    elif item == "√":
                        if index > 0 and not expression[index - 1] in operators:
                            result = [str(MerionesLib.root(MerionesLib.str_to_num(expression[index - 1]),
                                                           MerionesLib.str_to_num(expression[index + 1])))]
                            expression[index - 1:index + 2] = result
                            index -= 1
                        else:
                            result = [str(MerionesLib.root(2, MerionesLib.str_to_num(expression[index + 1])))]
                            expression[index:index + 2] = result

                    elif item == "!":
                        result = [str(MerionesLib.factorial(MerionesLib.str_to_num(expression[index - 1])))]
                        expression[index - 1:index + 1] = result
                        index -= 1

                    elif item == "ln":
                        result = [str(MerionesLib.ln(MerionesLib.str_to_num(expression[index + 1])))]
                        expression[index:index + 2] = result

                index += 1
        return MerionesLib.str_to_num(expression[0])
