class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cache = dict()
        self.capacity = capacity
        self.key_queue = []
    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.cache:
            #return self.cache[key] # lookup result
            print ("caught get {}".format(self.cache[key]))
        else:
            print ("-1 {}".format(key))
            
    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key in self.cache:
            self.cache[key] = value
            if key not in self.key_queue:
                self.key_queue.insert(key,key)
                print ("kq not in: {} cache key val {} {}".format(self.key_queue[key], key, self.cache[key]))
            else:
                self.key_queue.pop(self.key_queue.index(key,0,4))
                self.key_queue.insert(key, key)
                print ("kq in: {} cache key val {} {}".format(self.key_queue[key], key, self.cache[key]))
        else:
            if key not in self.key_queue and len(self.key_queue) == 5:
                self.key_queue.pop()
                self.key_queue.insert(key,key)

            self.cache[key] = value # put key in new spot.
        our_cache.prin()
        
    def prin(self):
        print ("KQ: {}".format(self.key_queue))

        
our_cache = LRU_Cache(5)

our_cache.set(1, 10)
our_cache.set(2, 20)

our_cache.get(1)       # returns 1
our_cache.get(2)        # returns 2

our_cache.get(3)       # return -1
#our_cache.set(1, 10)
our_cache.set(2, 20)
our_cache.set(3, 30)
our_cache.set(4, 40)
our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache
our_cache.set(5, 50) 
our_cache.set(6, 60)
our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

our_cache.prin()
