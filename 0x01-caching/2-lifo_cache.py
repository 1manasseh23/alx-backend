#!/usr/bin/python3
""" LIFOCache module
"""

from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """ Defines a LIFO caching system """

    def __init__(self):
        """ Initialize the LIFOCache instance """
        super().__init__()
        self.insertion_order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return
        
        if len(self.cache_data) >= self.MAX_ITEMS:
            # Find the last item added to the cache (most recent)
            last_key = self.insertion_order.pop()
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

        self.cache_data[key] = item
        self.insertion_order.append(key)

    def get(self, key):
        """ Get an item from the cache """
        if key is None:
            return None
        
        return self.cache_data.get(key, None)
