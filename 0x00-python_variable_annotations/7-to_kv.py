#!/usr/bin/env python3
"""Return a tuple module"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    to_kv - A function that takes str, int or float as argument.
    @k: String argumet
    @v: Int or float argument
    Returns: Tuple of string and float
    """
    return (k, v ** 2)
