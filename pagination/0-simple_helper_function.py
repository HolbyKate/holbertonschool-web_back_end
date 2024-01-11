#!/usr/bin/env python3
"""function named index_range that takes two integer arguments page and page_size"""

import pymongo


def index_range(page, page_size):
    """function named index_range that takes two integer arguments page and page_size"""
    return ((page - 1) * page_size, page * page_size)
