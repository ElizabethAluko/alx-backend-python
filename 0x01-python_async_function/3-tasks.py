#!/usr/bin/env python3
"""The module tasks an integer and returns asyncio.Task"""

import asyncio
from typing import Coroutine

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Taski:
    """Function take an integer and return asyncio.Task"""
    loop = asyncio.get_event_loop()
    task = loop.create_task(wait_random(max_delay))
    return task
