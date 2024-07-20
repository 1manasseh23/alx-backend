#!/usr/bin/env python3
"""This Implement a get_hyper method that takes the same
arguments (and defaults) as get_page and returns a dictionary
containing the following key-value pairs"""
import csv
from typing import List, Union
from math import ceil
from functools import lru_cache


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple of size two containing the start index and end index
    corresponding to the range of indexes to return in a list for the given
    pagination parameters.

    Page numbers are 1-indexed.
    """
    assert isinstance(page, int) and page > 0, \
        "Page must be a positive integer"
    assert isinstance(page_size, int) and page_size > 0, \
        "Page size must be a positive integer"

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    @lru_cache(maxsize=None)
    def dataset(self) -> List[List[str]]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header row
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """Returns a page of the dataset based on the pagination parameters"""
        dataset = self.dataset()
        total_rows = len(dataset)

        start_index, end_index = index_range(page, page_size)

        if start_index >= total_rows:
            return []  # Empty list if start_index is out of range

        # Adjust end_index if it exceeds total_rows
        end_index = min(end_index, total_rows)

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Returns hypermedia-style pagination information"""
        dataset_page = self.get_page(page, page_size)
        total_rows = len(self.dataset())

        page_size_actual = len(dataset_page)
        total_pages = ceil(total_rows / page_size)

        next_page = page + 1 if page * page_size < total_rows else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': page_size_actual,
            'page': page,
            'data': dataset_page,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
