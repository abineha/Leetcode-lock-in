import random

class Solution:

    def __init__(self, w: list[int]):
        self.prefix_sum = [0]
        
        for wi in w:
            self.prefix_sum.append(self.prefix_sum[-1]+wi)

    def pickIndex(self) -> int:
        target = self.prefix_sum[-1] * random.random()
        l, r = 0, len(self.prefix_sum)-1

        while l < r:
            m = (l+r) // 2

            if self.prefix_sum[m] <= target:
                l = m+1
            else:
                r = m
        
        return l-1


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()