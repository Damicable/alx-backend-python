#!/usr/bin/env python3
"""This module defines a regular function for creating an asyncio.Task"""


import asyncio
from typing import Task
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    task_wait_random - A function that defines random wait task
    @max_delay: Int. Max delay arg to random_wait
    Returns: Async task
    """
    return asyncio.create_task(wait_random(max_delay))
