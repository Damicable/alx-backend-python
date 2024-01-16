#!/usr/bin/env python3
"""Duck-type annotation function"""


from typing import List, Optional, TypeVar

T = TypeVar('T')


def safe_first_element(lst: List[T]) -> Optional[T]:
    """
    safe_first_element - function that returns the first element of a
    list if it exists.
    @lst: The input list.

    Returns: The first element of the list if it exists, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
