#!/usr/bin/env ython3
"""Duck-type annotation"""



def safe_first_element(lst):
    """
    A function that impements a duck-type annotation
    """
    if lst:
        return lst[0]
    else:
        return None
