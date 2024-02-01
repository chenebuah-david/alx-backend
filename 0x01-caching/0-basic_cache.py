#!/usr/bin/env python3
"""
The Basic ditionary module
"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    The basic Cache class that inherits from BaseCaching
    """

    def put(self, key, item):
        """
        This must assign the item value for the key
        the dictionary self.cache_data
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        This must return the value in self.cache_data linked to key
        """
        return self.cache_data.get(key, None)
