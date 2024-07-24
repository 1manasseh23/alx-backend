#!/usr/bin/python3
""" MRUCache module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ Defines a MRU caching system """

    def __init__(self):
        """ Initialize the MRUCache instance """
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        # Check if key already exists
        if key in self.cache_data:
            # Update existing key's item
            self.cache_data[key] = item
            # Move key to end of usage_order to mark it as recently used
            self.usage_order.remove(key)
            self.usage_order.append(key)
        else:
            # Add new key to cache
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Evict the most recently used item
                mru_key = self.usage_order.pop()
                del self.cache_data[mru_key]
                print(f"DISCARD: {mru_key}")

            self.cache_data[key] = item
            self.usage_order.append(key)

    def get(self, key):
        """ Get an item from the cache """
        if key is None:
            return None

        if key in self.cache_data:
            # Move key to end of usage_order to mark it as recently used
            self.usage_order.remove(key)
            self.usage_order.append(key)
            return self.cache_data[key]
        else:
            return None
