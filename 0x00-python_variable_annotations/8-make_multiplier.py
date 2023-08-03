#!/usr/bin/env python3
"""Contains a function to demostrate annotations - complex types"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float multiplier as an argument and returns a function
    that multiplies a float by multiplier.

    Parameters:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: The function that multiplies a
        float by the multiplier.
    """

    def multiply(value: float) -> float:
        """Returns the product of the value and multiplier"""

        return value * multiplier

    return multiply

