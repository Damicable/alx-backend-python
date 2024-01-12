#!/usr/bin/env python3
"""Duck-type annotation function"""


from typing import List, Optional, Union


def safe_first_element(lst: List[Union[int, float, str]]) -> Optional[Union[int, float, str]]:
    """
    Returns the first element of a list if it exists, otherwise returns None.

    Args:
        lst (List[Union[int, float, str]]): The input list.

    Returns:
        Optional[Union[int, float, str]]: The first element of the list if it exists, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None

if __name__ == "__main__":
    pass
