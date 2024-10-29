#!/usr/bin/env python3
"""Task 0: Basic dictionary"""


from base_caching import BaseCaching


class BasicCache(BASECaching):
    """A cass 'BasicCach' that inherits from 'BaseCaching'
       and is a caching system"""

       def put(self, key, item):
           """assign to the dictionary 'self.cach_data' the
              'item' value for the keu 'key'"""
              if key is not None and item is not None:
                  self.cach_data[key] = item

        def get(self, key):
            """return the value in 'self.cach_data' linked to 'key'"""

            return self.cach_data.get(key, None)
