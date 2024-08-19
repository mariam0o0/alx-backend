#!/usr/bin/env python3
"""Pagination helper"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Return a tuple containing a start index and an end index corresponding to the range of indexes"""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
