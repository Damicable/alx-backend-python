#!/usr/bin/env python3
"""Duck type annotation module"""


from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    element_length - Make multiplier
    @lst: returns tuples for each value and its length
    Return: List of tuples
    """
    return [(i, len(i)) for i in lst]
