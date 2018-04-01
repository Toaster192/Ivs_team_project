def factorial(self, n):
    """
    Method computes factorial of n

    @param n: number of which factorial is calculated
    @return: factorial of number n
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def power(self, base, exponent):
    """
    Method calculates a base raised to a power

    @param base: base of the power
    @param exponent: exponent determines how many times the base will be multiplied
    @return: base raised to the power
    """
    return base**exponent


def root(self, n):
    """
    Method calculates square root of n

    @param n: number of which square root will be calculate
    @return: square root of n
    """
    return n ** 0.5

def ln(self, x):
    """
    Method calculates natural logarithm of x

    @param x: number of which natural logarithm will be calculate
    @return: natural logarithm of x
    """
    n = 100000000.0
    return n * ((x ** (1/n)) - 1)


