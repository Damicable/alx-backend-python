#!/usr/bin/env python3
"""
This module defines an asynchronous routine and a regular function
for waiting for random delays.
"""


import asyncio
from typing import List, Task
from my_module import task_wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    task_wait_n - Function to execute the wait_random function
        a given number of times asynchronously using create_task
    @n: Int number of times to run the wait_random function
    @max_delay: Int argument to the wait_random function
    Returns: List of floats
    """
    delays = []
    for i in range(n):
        delays.append(await asyncio.create_task(wait_random(max_delay)))
    return sorted(delays)
