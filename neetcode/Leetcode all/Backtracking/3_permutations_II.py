from typing import List
from collections import defaultdict

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        perm = []
        map = defaultdict(int)

        for n in nums:
            map[n] += 1
        
        def dfs():
            if len(perm) == len(nums):
                result.append(perm.copy())
                return
        
            for n in map:
                if map[n] > 0:
                    perm.append(n)
                    map[n] -= 1
                    dfs()
                    map[n] += 1
                    perm.pop()
        
        dfs()
        return result