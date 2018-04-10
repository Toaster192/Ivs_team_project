from src.merionesmathlib import MerionesLib


def standard_deviation(numbers, n):
    x_dash = arithmetic_mean(numbers, n)
    left_side = MerionesLib.sub(n, 1)
    left_side = MerionesLib.div(1, left_side)
    right_side = MerionesLib.power(x_dash, 2)
    right_side = MerionesLib.mul(n, right_side)
    middle = arithmetic_mean([MerionesLib.power(float(number), 2) for number in numbers], n)
    right_side = MerionesLib.sub(middle, right_side)
    middle = MerionesLib.mul(left_side, right_side)
    print(MerionesLib.root(middle, 2))


def standard_deviation_one_liner(numbers, n):  # a one-liner version of the function above
    print(MerionesLib.root(                    # in case storing to variables is slower
        MerionesLib.mul(
            MerionesLib.div(
                1, MerionesLib.sub(
                    n, 1)), MerionesLib.sub(
                arithmetic_mean(
                    [MerionesLib.power(
                        float(number), 2)
                        for number in numbers], n),
                MerionesLib.mul(
                    n, MerionesLib.power(
                        arithmetic_mean(
                            numbers, n), 2)))), 2))


def arithmetic_mean(numbers, n):
    total = 0.
    for number in numbers:
        total = MerionesLib.add(total, float(number))
    return MerionesLib.div(total, n)


if __name__ == '__main__':
    string_input = input("Enter numbers for standard deviation (separated by a comma):")
    string_input = string_input.replace(" ", "").split(',')
    standard_deviation(string_input, len(string_input))
