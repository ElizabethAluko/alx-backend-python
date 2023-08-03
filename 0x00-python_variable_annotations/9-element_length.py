#!/usr/bin/env python3
"""Contains a function to demostrate iterable object  annotations"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes a list of sequences and returns a list of tuples.
    Each tuple contains an element from the input list and
    its corresponding length.

    Parameters:
        lst (Iterable[Sequence]): The input list of sequences.

    Returns:
        List[Tuple[Sequence, int]]: The list of tuples containing
        the element and its length.
    """
    return [(i, len(i)) for i in lst]
