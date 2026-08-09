#!/usr/bin/python3
"""100-matrix_mul module.

Defines a function that multiplies two matrices.
"""


def validate_matrix(m, name):
    """Validate that m is a proper rectangular matrix of numbers."""
    if not isinstance(m, list):
        raise TypeError("{} must be a list".format(name))

    if not all(isinstance(row, list) for row in m):
        raise TypeError("{} must be a list of lists".format(name))

    if len(m) == 0 or all(len(row) == 0 for row in m):
        raise ValueError("{} can't be empty".format(name))

    if not all(isinstance(n, (int, float))
               for row in m for n in row):
        raise TypeError(
            "{} should contain only integers or floats".format(name))

    if len(set(len(row) for row in m)) > 1:
        raise TypeError(
            "each row of {} must be of the same size".format(name))


def matrix_mul(m_a, m_b):
    """Multiply two matrices and return the resulting matrix."""
    validate_matrix(m_a, "m_a")
    validate_matrix(m_b, "m_b")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        new_row = []
        for j in range(len(m_b[0])):
            total = 0
            for k in range(len(m_b)):
                total += m_a[i][k] * m_b[k][j]
            new_row.append(total)
        result.append(new_row)

    return result
