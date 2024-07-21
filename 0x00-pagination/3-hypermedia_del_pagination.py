#!/usr/bin/env python3
""" a get_hyper_index method with two integer arguments: index with
a None default value and page_size with default value of 10

Return a dictionary with the following key-value pairs:
index: the current start index of the return page. That is the index of
the first item in the current page. For example if requesting page 3 with
page_size 20, and no data was removed from the dataset,
the current index should be 60.
next_index: the next index to query with. That should be the index of the
first item after the last item on the current page.
page_size: the current page size
data: the actual page of the dataset"""
import csv
import math
from typing import List, Dict  # Import Dict from typing module


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            # truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Returns hypermedia-style pagination information based on index"""
        indexed_dataset = self.indexed_dataset()
        total_rows = len(indexed_dataset)

        if index is None:
            index = 0

        assert isinstance(index, int) and 0 <= index < total_rows, \
            "Index is out of range"
        assert isinstance(page_size, int) and page_size > 0, \
            "Page size must be a positive integer"

        next_index = index + page_size
        data = []

        for i in range(index, min(next_index, total_rows)):
            if i in indexed_dataset:
                data.append(indexed_dataset[i])
        """
        if index == 0:
            data = [indexed_dataset[i] for i in range(
            min(page_size, total_rows))]
        else:
            data = [indexed_dataset[i] for i in range(
            index, min(next_index, total_rows))]
        """

        return {
            'index': index,
            'next_index': next_index if next_index < total_rows else None,
            'page_size': len(data),
            'data': data
        }
