from collections import Counter
import math

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        map = Counter(nums)
        result = 0

        for n, c in map.items():
            if c == 1:
                return -1
            result += math.ceil(c/3)
        
        return result