#!/usr/bin/env python3
"""Measure runtime module"""


import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure_runtime - Function to measure async comprehension runtime
    Return: Time it took to run
    """
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(async_comprehension(), async_comprehension(), async_comprehension(), async_comprehension())
    end_time = asyncio.get_event_loop().time()
    total_runtime = end_time - start_time
    return total_runtime
