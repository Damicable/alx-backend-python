#!/usr/bin/env python3
"""An  asynchronous coroutine module"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    wait_random - A function that wait for a random delay between
    0 and max_delay value 10
    @max_delay: The maximum delay.
    Return: Random delay in float
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


if __name__ == "__main__":
    asyncio.run(wait_random())
