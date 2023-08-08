#!/usr/bin/env python3
"""Tasjk 4"""

import asyncio
from typing import List

# Importing task_wait_random from task_wait_random.py
from task_wait_random import task_wait_random

async def task_wait_n(n: int, max_delay: float) -> List[float]:
    """ Task wait function"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
