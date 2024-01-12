#!/usr/bin/env python3
"""
Implement a method named get_page that takes two integer arguments page
with default value 1 and page_size with default value 10
"""

import builtins
import csv
import math
import random
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        method named get_page that takes two integer arguments page
        with default value 1 and page_size with default value 10.
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        range = index_range(page, page_size)
        return self.dataset()[range[0]:range[1]]


    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        method that takes the same arguments (and defaults) as get_page
        and returns a dictionary containing the following key-value pairs
        """
        data = self.get_page(page, page_size)
        return {
            "page_size": len(data),
            "page": page,
            "data": dataset,
            "next_page": page + 1 if page + 1 < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }


def index_range(page: int, page_size: int):
    """
    function named index_range that takes two integer
    arguments page and page_size
    """
    return ((page - 1) * page_size, page * page_size)
