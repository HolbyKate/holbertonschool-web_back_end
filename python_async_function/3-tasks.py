#!/usr/bin/env python3
"""
Write a function (do not create an async function, use the regular function
syntax to do this) task_wait_random that takes an integer max_delay
and returns a asyncio.Task
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Returns a random delay between 0 and max_delay"""
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return (random_delay)


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """Returns asyncio.Task"""
    return asyncio.Task(wait_random(max_delay))
