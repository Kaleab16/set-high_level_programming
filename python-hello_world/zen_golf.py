#!/usr/bin/python3
"""
AI Refactoring: The Zen of Python
"""


def sum_even_verbose(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total = total + num
    return total


def longest_word_verbose(words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


def filter_positive_verbose(numbers):
    result = []
    for num in numbers:
        if num > 0:
            result.append(num)
    return result
# Pythonic version
# Zen: Simple is better than complex.
# Zen: Readability counts.
def sum_even_pythonic(numbers):
    return sum(num for num in numbers if num % 2 == 0)


# Pythonic version
# Zen: There should be one—and preferably only one—obvious way to do it.
def longest_word_pythonic(words):
    return max(words, key=len, default="")


# Pythonic version
# Zen: Beautiful is better than ugly.
# Zen: Readability counts.
def filter_positive_pythonic(numbers):
    return [num for num in numbers if num > 0]
