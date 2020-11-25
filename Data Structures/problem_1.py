from collections import OrderedDict

class LRU_Cache(object):
    def __init__(self, capacity):
        # Initialize class variables
        self.cache_odict = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key not in self.cache_odict:
            print("-1")
            return -1
        else:
            #add the key to the end of list
            self.cache_odict.move_to_end(key)
            print(self.cache_odict[key])
            return self.cache_odict[key]

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        self.cache_odict[key] = value
        self.cache_odict.move_to_end(key)
        if len(self.cache_odict) > self.capacity:
            self.cache_odict.popitem(last = False)

our_cache = LRU_Cache(5)
our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);
print(our_cache.cache_odict)
#Testcase 1
our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
#Testcase 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache
#Testcase 3
print(our_cache.cache_odict)
our_cache.set(5, 5)
print(our_cache.cache_odict)
our_cache.set(6, 6)
print(our_cache.cache_odict)
our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print(our_cache.cache_odict)

our_cache=LRU_Cache(3)
our_cache.set(1,1)
our_cache.set(2,2)
our_cache.set(3,3)
print(our_cache.cache_odict)
our_cache.set(4,4)
print(our_cache.cache_odict)
our_cache.get(4)   # Expected Value = 4
print(our_cache.cache_odict)
our_cache.get(1)   # Expected Value = -1
print(our_cache.cache_odict)
our_cache.set(2,4)
print(our_cache.cache_odict)
our_cache.get(2)   # Expected Value = 4
print(our_cache.cache_odict)
our_cache.set(5,5)
print(our_cache.cache_odict)
print(our_cache.get(3))   # Expected Value = -1 Your Output = 3
print(our_cache.cache_odict)

#Testcase Requested by reviewer:
our_cache=LRU_Cache(0)
print(our_cache.cache_odict) #prints empty cache
our_cache.get(1)    # Expected value = -1
our_cache.set(1, 1) # When cache is empty all values will bounce and not get stored for retrival
print(our_cache.cache_odict) # cache should remain empty or size zero
our_cache.get(1)    # Expected value = -1
