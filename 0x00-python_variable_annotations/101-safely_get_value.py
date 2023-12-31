#!/usr/bin/env python3
"""add type annotations to the function TypeVar"""
from typing import Mapping, TypeVar, Any, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None)\
        -> Union[Any, T]:
    """TypeVar"""
    if key in dct:
        return dct[key]
    else:
        return default
