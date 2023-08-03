#!/usr/bin/env python3
"""Contains a function to demostrate iterable object  annotations"""
from typing import TypeVar, Mapping, Any, Union
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely get the value associated with the given key from the
    dictionary.

    Parameters:
        dct (Mapping): The input dictionary.
        key (Any): The key to search in the dictionary.
        default (Optional[T]): The default value to return if the
        key is not found (default is None).

    Returns:
        Union[Any, T]: The value associated with the key in the
        dictionary if found, else the default value.
    """

    if key in dct:
        return dct[key]
    else:
        return default
