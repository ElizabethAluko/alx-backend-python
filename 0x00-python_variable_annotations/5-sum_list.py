#!/usr/bin/env python3
"""Contains a function to demostrate annotations - lists of float"""


def sum_list(input_list: list[float]) -> float:
    """
    Add the lists items of a list
    input_list: the list to sum its items.
    """
    sum_of_list: float = 0.0

    for i in range(len(input_list)):
        sum_of_list += i
    return (sum_of_list)
