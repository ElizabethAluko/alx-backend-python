#!/usr/bin/env python3
"""Task 3"""

import asyncio
from typing import Coroutine

# Importing wait_random from 0-basic_async_syntax.py
wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    loop = asyncio.get_event_loop()
    task = loop.create_task(wait_random(max_delay))
    return task
