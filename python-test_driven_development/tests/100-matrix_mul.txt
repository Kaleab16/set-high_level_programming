The ``100-matrix_mul`` module
===============================

Using ``matrix_mul``
----------------------

Import the function:

    >>> matrix_mul = __import__('100-matrix_mul').matrix_mul

Basic square matrix multiplication:

    >>> matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
    [[7, 10], [15, 22]]

Non-square compatible matrices:

    >>> matrix_mul([[1, 2]], [[3, 4], [5, 6]])
    [[13, 16]]

m_a is not a list:

    >>> matrix_mul(42, [[1, 2]])
    Traceback (most recent call last):
    TypeError: m_a must be a list

m_a is not a list of lists:

    >>> matrix_mul([1, 2], [[1, 2]])
    Traceback (most recent call last):
    TypeError: m_a must be a list of lists

m_a is empty:

    >>> matrix_mul([[]], [[1, 2]])
    Traceback (most recent call last):
    ValueError: m_a can't be empty

Matrices can't be multiplied due to incompatible dimensions:

    >>> matrix_mul([[1, 2], [3, 4]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    Traceback (most recent call last):
    ValueError: m_a and m_b can't be multiplied
