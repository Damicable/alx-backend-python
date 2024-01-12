#!/usr/bin/env python3
"""A type annotiontio function"""


from typing import TypeVar, Dict, Any

T = TypeVar('T')


def safely_get_value(dct: Dict[str, T], key: str, default: T = None) -> T:
    """
    safely_get_value - Function that safely retrieves a value from a
    dictionary based on the key.
    @dct: The input dictionary.
    @key: The key to retrieve the value from.
    @default: The default value to return if the key is not present
    Returns: The value associated with the key if it exists, otherwise
    the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default

if __name__ == "__main__":
    pass
