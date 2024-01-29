#!/usr/bin/env python3
"""
The Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """The server class to paginate
       a database of popular baby names
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """The cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """This is the dataset indexed by sorting
           position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                j: dataset[j] for j in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """This returns a dictionary"""
        assert type(index) == int and type(page_size) == int
        assert 0 <= index < len(self.indexed_dataset())
        pages = []
        next_index = index + page_size
        for j in range(index, index + page_size):
            if not self.indexed_dataset().get(j):
                j += 1
                next_index += 1
            pages.append(self.indexed_dataset()[j])
        return {'index': index,
                'next_index': next_index,
                'page_size': page_size,
                'data': pages
                }
