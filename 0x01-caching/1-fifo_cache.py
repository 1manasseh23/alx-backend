#!/usr/bin/python3
""" FIFOCache module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ Defines a FIFO caching system """

    def __init__(self):
        """ Initialize the FIFOCache instance """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            # Find the first item added to the cache (oldest)
            oldest_key = next(iter(self.cache_data))
            del self.cache_data[oldest_key]
            print(f"DISCARD: {oldest_key}")

        self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache """
        if key is None:
            return None

        return self.cache_data.get(key, None)
