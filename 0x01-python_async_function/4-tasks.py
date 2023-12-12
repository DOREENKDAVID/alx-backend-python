#!/usr/bin/env python3
"""create task"""


import asyncio
from typing import List, Callable

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """execute multiple coroutines at the same time with async
    mandatory"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
