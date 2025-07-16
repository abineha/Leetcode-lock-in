import random

class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.map[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        idx = self.map[val]
        lastval = self.list[-1]
        self.list[idx] = lastval
        self.map[lastval] = idx
        self.list.pop()
        del self.map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.list)
