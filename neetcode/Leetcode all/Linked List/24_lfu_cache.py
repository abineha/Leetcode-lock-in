from collections import defaultdict

class ListNode:
    # Node for the doubly linked list
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class LinkedList:
    # Doubly linked list with dummy left/right nodes + hashmap for O(1) access
    def __init__(self):
        # Dummy left and right to simplify insert/remove
        self.left = ListNode(0)
        self.right = ListNode(0, self.left)
        self.left.next = self.right
        # Map value -> node (for O(1) removal)
        self.map = {}

    def length(self):
        # Current number of nodes (excluding dummy nodes)
        return len(self.map)

    def pushRight(self, val):
        # Insert new node just before the right dummy
        node = ListNode(val, self.right.prev, self.right)
        self.map[val] = node
        self.right.prev = node
        node.prev.next = node

    def pop(self, val):
        # Remove node with given val from list + map
        if val in self.map:
            node = self.map[val]
            next, prev = node.next, node.prev
            next.prev = prev
            prev.next = next
            self.map.pop(val, None)

    def popLeft(self):
        # Remove and return the first real node (after left dummy)
        res = self.left.next.val
        self.pop(self.left.next.val)
        return res

    def update(self, val):
        # Move existing val to the rightmost position (most recently used in this freq bucket)
        self.pop(val)
        self.pushRight(val)


class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity              # Max capacity of cache
        self.lfuCnt = 0                  # Current minimum frequency count among keys
        self.valMap = {}                 # key -> value
        self.countMap = defaultdict(int) # key -> frequency
        self.listMap = defaultdict(LinkedList) # frequency -> linkedlist of keys

    def counter(self, key):
        # Update frequency of a key when it's accessed
        cnt = self.countMap[key]
        self.countMap[key] += 1

        # Remove key from current frequency list
        self.listMap[cnt].pop(key)
        # Add key to next higher frequency list
        self.listMap[cnt + 1].pushRight(key)

        # If this key was the only one in the min frequency list, increment lfuCnt
        if cnt == self.lfuCnt and self.listMap[cnt].length() == 0:
            self.lfuCnt += 1

    def get(self, key: int) -> int:
        # Return value if key exists, else -1
        if key not in self.valMap:
            return -1
        self.counter(key) # Increase frequency count
        return self.valMap[key]

    def put(self, key: int, value: int) -> None:
        if self.cap == 0: # No capacity, can't put
            return

        # If key not present and cache is full, evict LFU key
        if key not in self.valMap and len(self.valMap) == self.cap:
            res = self.listMap[self.lfuCnt].popLeft() # LFU + LRU eviction
            self.valMap.pop(res)
            self.countMap.pop(res)

        # Insert or update key->value
        self.valMap[key] = value
        self.counter(key) # Update frequency
        # Ensure lfuCnt stays in sync with the lowest frequency
        self.lfuCnt = min(self.lfuCnt, self.countMap[key])
