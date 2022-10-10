from collections import OrderedDict


class LruCache:

    def __int__(self, size):
        self.orderedDict = OrderedDict
        self.size = size

    def add(self, key, value):
        self.orderedDict[key] = value
        self.orderedDict.move_to_end(key)
        if len(self.orderedDict) > self.size:
            self.orderedDict.popitem(last=False)

    def get(self, key):
        if key not in self.orderedDict:
            return -1
        else:
            self.orderedDict.move_to_end(key)
            return self.orderedDict[key]

# Use an ordered dictionary
# When getting, move the pair to the end of the dictionary
# When adding, move the pair to the end of the dictionary
#   If the cache is full, then evict the top of pair
