#!/usr/bin/env python3
"""Task 4 module of the project"""

import asyncio
from typing import List

task_wait_random =  __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: float) -> List[float]:
    """ Task wait function"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
