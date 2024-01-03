#!/usr/bin/env python3
"""
import wait_n and create a measure_time function with integers n and
max_delay as arguments that measures the total execution time for
wait_n(n, max_delay), and returns total_time / n
"""


import asyncio
import random
from typing import List


async def wait_random(max_delay: int = 10) -> float:
    """Returns a random delay between 0 and max_delay"""
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return (random_delay)


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Returns list of all delays in ascending order"""
    delays = []
    for i in range(n):
        delays.append(await wait_random(max_delay))
    return sorted(delays)


def measure_time(n: int, max_delay: int) -> float:
    """Returns average time of wait_n"""
    total_time = asyncio.run(wait_n(n, max_delay))
    return sum(total_time) / n
