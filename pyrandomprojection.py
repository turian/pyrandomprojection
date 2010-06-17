#!/usr/bin/python
"""
Random projection library for Python, converting a dictionary to
low-dimensional numpy vector
"""

#import math
#import murmur
import numpy
from common.deterministicrandom import deterministicrandom
import common.gaussian

def project(dict, dimensions, RANDOMIZATION_TYPE="gaussian", TERNARY_NON_ZERO_PERCENT=None, RANDOM_SEED=0):
    """
    Project dict to a numpy vector with a specified number of dimensions.
    RANDOMIZATION_TYPE: Either "ternary" (-1, 0, +1) or "gaussian" random matrix.
    TERNARY_NON_ZERO_PERCENT: float in range (0.0, 1.0), percent of elements in random matrix that are non-zero.
    """
    projection = numpy.zeros((dimensions,))

    for key, value in dict.items():
        projection += value * randomrow(key, dimensions, RANDOMIZATION_TYPE, TERNARY_NON_ZERO_PERCENT, RANDOM_SEED)

    return projection

def randomrow(key, dimensions, RANDOMIZATION_TYPE="gaussian", TERNARY_NON_ZERO_PERCENT=None, RANDOM_SEED=0):
    """
    Access the random matrix row corresponding to key, with a certain
    number of dimensions.

    RANDOMIZATION_TYPE: Either "ternary" (-1, 0, +1) or "gaussian" random matrix.
    TERNARY_NON_ZERO_PERCENT: float in range (0.0, 1.0), percent of elements in random matrix that are non-zero.
    """
    if RANDOMIZATION_TYPE == "gaussian":
        values = []
        for i in range(dimensions):
            # Unique name for this matrix entry
            matrix_entry_name = `key` + "-" + `i` + "-" + `RANDOM_SEED`

            matrix_entry_name_random = deterministicrandom(matrix_entry_name)
            gaussian_value = common.gaussian.from_probability(matrix_entry_name_random)

            values.append(gaussian_value)
        numpy_values = numpy.array(values)
        assert numpy_values.shape == (dimensions,)
#        print numpy.mean(foo)
#        print numpy.var(foo)
#        print numpy.std(foo)
        return numpy_values
    elif RANDOMIZATION_TYPE == "ternary":
        assert TERNARY_NON_ZERO_PERCENT > 0.0 and TERNARY_NON_ZERO_PERCENT < 1.0
        assert 0        # Not yet implemented
    else: assert 0

if __name__ == "__main__":
    dict = {"cool": 10, "boy": 20}
    print project(dict, 100)
