#!/usr/bin/env python3
"""
Module for BasicCache class that inherits from BaseCaching
"""
BaseCaching = __import__('0-basic_cache').BaseCaching


class BasicCache(BaseCaching):
    """
    A caching system that doesn't have a limit.
    """

    def put(self, key, item):
        """
        Assigns the item value for the key key in the cache.

        Args:
            key: The key to store the item under.
            item: The item to be stored.

        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value in the cache linked to the provided key.

        Args:
            key: The key to retrieve the value for.

        Returns:
            The value associated with the key if it exists, otherwise None.

        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
