#!/usr/bin/python3
"""Module that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Find a peak value in a list of integers.

    A peak is an element that is greater than or equal to its
    neighbors. Uses a binary search approach for O(log(n))
    complexity instead of scanning the entire list.

    Args:
        list_of_integers (list): The list of integers to search.

    Returns:
        int: A peak value in the list, or None if the list is empty.
    """
    if not list_of_integers:
        return None

    low = 0
    high = len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return list_of_integers[low]
