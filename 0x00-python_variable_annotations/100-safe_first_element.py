#!/usr/bin/env python3
"""Contains a function to demostrate iterable object  annotations"""
from typing import Union, Sequence


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Take sequence of any type and return Any type or none"""
    if lst:
        return lst[0]
    else:
        return None
