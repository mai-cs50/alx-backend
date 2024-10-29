#!/usr/bin/python3
"""Task 2: LIFO caching"""


from collections import OrderedDict

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """A class 'FIFOCache' that inherits from
       'BaseCaching' and is a caching system"""

       def __init__(self):
           """Initializes the cache"""
           super().__init__()
           self.cache_data = OrderedDict()

        def put(self, key, item):
            """assign to the dictionary 'self.cach_data' the
               'item' value for the key 'key'"""

               if key is None or item is None:
                   return
               if key not in self.cache_data:
                   if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                       last_key, _ = self.cache_data.popitem(True)
                       print("DISCARD:", last_key)

                    self.cache_data[key] = item
                    self.cache_data.move_to_end(key, last=True)

        def get(self, key):
            """Retrieves an item by key"""
            return self.cache_data.get(key, None)
