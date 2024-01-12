#!/usr/bin/env python3
"""Sum mixed list function module"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    sum_mixed_list - A function that sums a mixed list of floats
    @mxd_lst: List of mixed floats and integers
    Return: Float
    """
    return float(sum(mxd_lst))
