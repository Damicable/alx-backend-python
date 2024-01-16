#!/usr/bin/env python3
"""Measuring runtime module"""


import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measure_time - Function to measure the time wait_n takes to run
    @n: Int, Number of times to run the wait function
    @max_delay: Int, Maximum of range to choose random delay period from
    Returns: Total time divided by n
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    return total_time / n
