#!/usr/bin/env python3
"""This Implement a method named get_page that takes
two integer arguments page with default value 1 and
page_size with default value 10"""
import csv
import math
from typing import List


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

    def index_range(self, page: int, page_size: int) -> tuple:
        """
        Returns a tuple of size two containing a start index and an end index
        corresponding to the range of indexes to return in a list for those
        particular pagination parameters.
        """
        assert isinstance(page, int) and page > 0, \
            "Page must be a positive integer."
        assert isinstance(page_size, int) and page_size > 0, \
            "Page size must be a positive integer."

        dataset = self.dataset()
        total_items = len(dataset)

        start_index = (page - 1) * page_size
        end_index = page * page_size

        return (start_index, end_index)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Returns a list of lists representing the corresponding page
        containing the desired number of items.
        """
        assert isinstance(page, int) and page > 0, \
            "Page must be a positive integer."
        assert isinstance(page_size, int) and page_size > 0, \
            "Page size must be a positive integer."

        dataset = self.dataset()
        total_items = len(dataset)

        start_index, end_index = self.index_range(page, page_size)

        if start_index >= total_items:
            return []

        return dataset[start_index:end_index]
