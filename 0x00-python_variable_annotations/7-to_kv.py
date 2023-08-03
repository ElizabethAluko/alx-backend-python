#!/usr/bin/env python3
"""Contains a function to demostrate annotations - complex types"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Taka a string and an int/float and return a tuple.

    parameters:
    k: a string.
    v: int or float to be squared.

    Return:
        tuple: of k and square of v
    """
    return (k, float(v) ** 2)
