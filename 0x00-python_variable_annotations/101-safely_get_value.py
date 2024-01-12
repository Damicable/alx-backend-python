#!/usr/bin/env python3


from typing import TypeVar, Dict, Any

T = TypeVar('T')


def safely_get_value(dct: Dict[str, T], key: str, default: T = None) -> T:
    """
    Safely retrieves a value from a dictionary based on the key.

    Args:
        dct (Dict[str, T]): The input dictionary.
        key (str): The key to retrieve the value from.
        default (T, optional): The default value to return if the key is not present. Defaults to None.

    Returns:
        T: The value associated with the key if it exists, otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default

if __name__ == "__main__":
    pass
