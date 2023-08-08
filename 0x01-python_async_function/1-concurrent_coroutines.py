#!/usr/bin/env python3
"""Contain delay module that Import wait_random"""
import asyncio
import random
from typing import List

wait_random = __import__ ('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """For time delay"""

    tasks = [wait_random(max_delay) for i in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
