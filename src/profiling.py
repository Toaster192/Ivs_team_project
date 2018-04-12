#!/usr/bin/python
# -*- coding: utf-8 -*-

from merionesmathlib import MerionesLib


def standard_deviation(numbers, n):
    return MerionesLib.parse_parentheses("√(1 / ({} - 1) * ({} - {} * ((1 / {}) * {})^2))".format(
        n,
        total_of([MerionesLib.power(float(number), 2) for number in numbers]),
        n,
        n,
        total_of(numbers))
    )


def total_of(numbers):
    total = "("
    for number in numbers:
        total += str(number) + "+"
    return total[:-1] + ")"


if __name__ == '__main__':
    string_input = ""
    string_input = input("Enter numbers for standard deviation (separated by a comma):")
    string_input = str(string_input)[1:-1].replace(" ", "").split(',')
    print(standard_deviation(string_input, len(string_input)))
