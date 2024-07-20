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
from typing import List, Dict
import csv


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
            self.__dataset = dataset[1:]  # skip header row
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        dataset = self.indexed_dataset()

        if index is None:
            index = 0

        assert 0 <= index < len(dataset), "Index out of range"

        current_index = index
        data = []
        while len(data) < page_size and current_index < len(dataset):
            if current_index in dataset:
                data.append(dataset[current_index])
            current_index += 1

        next_index = current_index if current_index < len(dataset) else None

        return {
            'index': index,
            'data': data,
            'page_size': page_size,
            'next_index': next_index
        }
