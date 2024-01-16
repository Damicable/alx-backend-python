#!/usr/bin/env python3
"""
This module defines an asynchronous generator coroutine that yields random numbers.
"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator coroutine that yields random numbers.

    Yields:
        int: Random number between 0 and 10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
