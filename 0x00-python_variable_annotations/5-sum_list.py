#!/usr/bin/env python3
"""Contains a function to demostrate annotations - lists of float"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Add the lists items of a list

    parameters:
    input_list: the list to sum its items.

    return:
        float: sum of the items
    """
    return sum(input_list)
