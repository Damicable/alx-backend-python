#!/usr/bin/env python3
"""Duck-type annotation function"""


from typing import List, Optional, Union


def safe_first_element(lst: List[Union[int, float, str]]) -> Optional[Union[int, float, str]]:
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

if __name__ == "__main__":
    pass
