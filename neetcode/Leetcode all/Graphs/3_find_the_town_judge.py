from collections import defaultdict
from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inside, out = defaultdict(int), defaultdict(int)

        for s, d in trust:
            out[s] += 1
            inside[d] += 1
        
        for i in range(1, n+1):
            if out[i] == 0 and inside[i] == n-1:
                return i
            
        return -1