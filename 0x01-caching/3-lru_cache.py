#!/usr/bin/python3
""" LRUCache module
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ Defines a LRU caching system """

    def __init__(self):
        """ Initialize the LRUCache instance """
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
                # Evict the least recently used item
                lru_key = self.usage_order.pop(0)
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")

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
