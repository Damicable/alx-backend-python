#!/usr/bin/env python3
"""Multiplier function module"""

froom typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    make_multiplier - A functio that multily a float by multiplier
    @multiplier: Number that multiplies the float
    Return: Returns a function multiplying the arg with a float
    """
    return lambda x: x * multiplier
