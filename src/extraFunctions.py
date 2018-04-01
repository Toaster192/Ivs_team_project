def convert_weight(self, x, units):
    """
    Method converts number x to units given by parameter units

    @param x: number of kilograms
    @param units: units that user requested
    @return: number x converted to given units
    """
    if units == 'mg':
        return x * 1000 ** 2
    elif units == 'g':
        return x * 1000
    elif units == 'lb':
        return x * 2.20
    elif units == 't':
        return x * 0.001


def convert_length(self, x, units):
    """
    Method converts number x to units given by parameter units

    @param x: number of kilometers
    @param units: units that user requested
    @return: number x converted to given units
    """
    if units == 'm':
        return x * 1000
    elif units == 'cm':
        return x * 100000
    elif units == 'mm':
        return x * 1000**2
    elif units == 'mi':
        return x * 0.62137199


def convert_time(self, x, units):
    """
    Method converts number x to units given by parameter units

    @param x: number of hours
    @param units: units that user requested
    @return: number x converted to given units
    """
    if units == 'min':
        return x * 60
    elif units == 's':
        return x * 3600
    elif units == 'day':
        return x * 0.0416667


def convert_degrees(self, x, units):
    """
    Method converts number x to units given by parameter units

    @param x: number of celsius
    @param units: units that user requested
    @return: number x converted to given units
    """
    if units == 'K':
        return x + 273.15
    elif units == 'F':
        return (x * 9/5) + 32

















