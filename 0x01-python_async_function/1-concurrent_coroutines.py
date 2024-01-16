#!/usr/bin/env python3
"""An asynchronous coroutine for generating random delay concurently"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    wait_n - A function that executes the wait_random function
    a given number of times asynchronously
    @n: Int number of times to run the wait_random function
    @max_delay: Int argument to the wait_random function
    Returns: List of floats
    """
    delays = []
    for i in range(n):
        delays.append(await wait_random(max_delay))
    return sorted(delays)
