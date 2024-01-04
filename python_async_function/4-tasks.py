#!/usr/bin/env python3
"""Take the code from wait_n and alter it into a new function task_wait_n.
The code is nearly identical to wait_n except task_wait_random is being called
"""


import asyncio
import random
from typing import List


async def wait_random(max_delay: int = 10) -> float:
    """Returns a random delay between 0 and max_delay"""
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return (random_delay)


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Returns list of all delays in ascending order"""
    delays = []
    for i in range(n):
        delays.task(await wait_random(max_delay))
    return sorted(delays)
