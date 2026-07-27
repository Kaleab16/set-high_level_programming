#!/usr/bin/python3
"""
Measure and compare verbose vs Pythonic functions.
"""

import inspect
from zen_golf import *


def count_characters(code):
    """Count non-space, non-newline characters."""
    return len(code.replace(" ", "").replace("\n", ""))


def avg_line_length(code):
    """Average length of non-empty lines."""
    lines = [line for line in code.split("\n") if line.strip()]
    if not lines:
        return 0
    return sum(len(line) for line in lines) / len(lines)


def reduction_percentage(verbose, pythonic):
    """Calculate character reduction percentage."""
    return ((verbose - pythonic) / verbose) * 100


def compare(name, verbose_func, pythonic_func):
    verbose_code = inspect.getsource(verbose_func)
    pythonic_code = inspect.getsource(pythonic_func)

    verbose_chars = count_characters(verbose_code)
    pythonic_chars = count_characters(pythonic_code)

    verbose_read = avg_line_length(verbose_code)
    pythonic_read = avg_line_length(pythonic_code)

    print("=" * 60)
    print(name)
    print("=" * 60)

    print(f"Verbose characters : {verbose_chars}")
    print(f"Pythonic characters: {pythonic_chars}")
    print(f"Reduction          : {reduction_percentage(verbose_chars, pythonic_chars):.2f}%")

    print()

    print(f"Verbose avg line length : {verbose_read:.2f}")
    print(f"Pythonic avg line length: {pythonic_read:.2f}")

    print()


def test_equivalence():
    assert sum_even_verbose([1,2,3,4,5,6]) == sum_even_pythonic([1,2,3,4,5,6])

    assert longest_word_verbose(
        ["cat", "elephant", "dog", "whale"]
    ) == longest_word_pythonic(
        ["cat", "elephant", "dog", "whale"]
    )

    assert filter_positive_verbose(
        [-3,-1,0,2,5,-7]
    ) == filter_positive_pythonic(
        [-3,-1,0,2,5,-7]
    )

    print("✓ All functions produce identical results.\n")


if __name__ == "__main__":
    test_equivalence()

    compare(
        "Sum Even",
        sum_even_verbose,
        sum_even_pythonic
    )

    compare(
        "Longest Word",
        longest_word_verbose,
        longest_word_pythonic
    )

    compare(
        "Filter Positive",
        filter_positive_verbose,
        filter_positive_pythonic
    )
