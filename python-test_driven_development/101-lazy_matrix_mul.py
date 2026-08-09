#!/usr/bin/python3
"""101-lazy_matrix_mul module.

Defines a function that multiplies two matrices using NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using numpy, letting numpy validate shapes."""
    return np.array(m_a).dot(np.array(m_b))
