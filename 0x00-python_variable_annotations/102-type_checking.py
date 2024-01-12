#!/usr/bin/env python3
"""A function validation with mypy"""


from typing import Tuple, Any


def zoom_array(lst: Tuple[Any], factor: int = 2) -> Tuple[Any]:
    """
    A function that zooms into the array by repeating each element based
    on the specified factor.

    Args:
        lst (Tuple[Any]): The input array.
        factor (int, optional): The zoom factor. Defaults to 2.

    Returns:
        Tuple[Any]: The zoomed-in array.
    """
    zoomed_in: Tuple[Any] = tuple(
        item for item in lst
        for i in range(factor)
    )
    return zoomed_in

if __name__ == "__main__":
    array = (12, 72, 91)

    zoom_2x = zoom_array(array)

    # The correct way to call the function with a float factor
    zoom_3x = zoom_array(array, int(3.0))
