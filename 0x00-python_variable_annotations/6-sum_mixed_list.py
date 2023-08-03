#!/usr/bin/env python3
"""Contains a function to demostrate annotations - mixed lists"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """
    Add the lists items of a list

    parameters:
    mxd_lst: the list to sum its items.

    return:
        float: sum of the items
    """
    return sum(mxd_lst)
