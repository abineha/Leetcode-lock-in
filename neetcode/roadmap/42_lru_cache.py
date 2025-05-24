class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}    # map key <-> nodes

        self.L, self.R = Node(0,0), Node(0,0)    # L -> LRU, R -> MRU
        self.L.next, self.R.prev = self.R, self.L    # L <-> R

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])    # remove from double LL and add left of MRU
            self.insert(self.cache[key])    # as it is most recent accessed 
            return self.cache[key].val  
        return -1
    
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def insert(self, node):
        prev, next = self.R.prev, self.R
        prev.next = next.prev = node
        node.next, node.prev = next, prev
   
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.L.next    # delete LRU
            self.remove(lru)
            del self.cache[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)