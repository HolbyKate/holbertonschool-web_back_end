#!/usr/bin/env python3
"""
Write an async routine called wait_n that takes in 2 int arguments
(in this order): n and max_delay. You will spawn wait_random n times
with the specified max_delay
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
