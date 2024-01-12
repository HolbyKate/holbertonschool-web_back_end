#!/usr/bin/env python3
"""
function named index_range that takes two integer arguments
page and page_size
"""
import builtins


def index_range(page: int, page_size: int):
    """
    function named index_range that takes two integer
    arguments page and page_size
    """
    return ((page - 1) * page_size, page * page_size)
