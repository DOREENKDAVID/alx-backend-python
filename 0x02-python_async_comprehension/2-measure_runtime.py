#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""


import asyncio
import random
from typing import List
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Execute async_comprehension four times in parallel"""
    start_time = asyncio.get_event_loop().time()

    # execute 4 times in parallel#
    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
            )
    end_time = asyncio.get_event_loop().time()
    total_runtime = end_time - start_time
    return total_runtime
