#!/usr/bin/env python3
"""Contains a function to demostrate iterable object  annotations"""
from typing import Union, Sequence, Any


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Return the first element of the input list if it's not empty,
    otherwise return None.

    Parameters:
        lst (Sequence[Any]): The input list of any type of elements.

    Returns:
        Union[Any, None]: The first element of the list if not
        empty, else None.
    """
    if lst:
        return lst[0]
    else:
        return None
