class LRU_Cache(object):
    def __init__(self, capacity):
        # Initialize class variables
        self.cache_values = []
        self.cache_dict = {}
        self.capacity = capacity
        self.num_entries = 0

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key not in self.cache_dict:
            print("-1")
            return -1
        else:
            #pop the key out
            pop_value = self.cache_dict.pop(key)
            self.cache_values.remove(pop_value)
            #add the key to the end of list
            self.cache_dict[key] = pop_value
            self.cache_values.append(pop_value)
            print(pop_value)
            return pop_value

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key in self.cache_dict:
            #self.cache_values.remove(value)
            self.cache_values.remove(self.cache_dict[key])
            del self.cache_dict[key]
            self.num_entries -= 1
        elif (self.num_entries >= self.capacity):
            #perform LRU: pop the first element of list out
            first_list_value = self.cache_values.pop(0)
            dict_value = self.cache_dict.pop(first_list_value)
            self.num_entries -= 1
        self.cache_dict[key] = value
        self.cache_values.append(value)
        self.num_entries += 1

our_cache = LRU_Cache(5)
our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);
print(our_cache.cache_values)
#Testcase 1
our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
#Testcase 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache
#Testcase 3
print(our_cache.cache_values)
our_cache.set(5, 5)
print(our_cache.cache_values)
our_cache.set(6, 6)
print(our_cache.cache_values)
our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print(our_cache.cache_values)

our_cache=LRU_Cache(3)
our_cache.set(1,1)
our_cache.set(2,2)
our_cache.set(3,3)
print(our_cache.cache_values)
our_cache.set(4,4)
print(our_cache.cache_values)
our_cache.get(4)   # Expected Value = 4
print(our_cache.cache_values)
our_cache.get(1)   # Expected Value = -1
print(our_cache.cache_values)
our_cache.set(2,4)
print(our_cache.cache_values)
our_cache.get(2)   # Expected Value = 4
print(our_cache.cache_values)
our_cache.set(5,5)
print(our_cache.cache_values)
print(our_cache.get(3))   # Expected Value = -1 Your Output = 3
print(our_cache.cache_values)
