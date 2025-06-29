class MyHashSet:
    #   1000000 / 32 = 31250 buckets needed
    # key is in the range [1, 1000000]
    # 31251 * 32 = 1000032
    
    def __init__(self):
        self.set  = [0] * 31251

    def add(self, key: int) -> None:
        self.set[key//32] |= self.mask(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
           self.set[key//32] ^= self.mask(key)

    def contains(self, key: int) -> bool:
        return self.set[key//32] & self.mask(key) != 0

    def mask(self, key: int) -> int:
        return 1 << (key % 32)
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)