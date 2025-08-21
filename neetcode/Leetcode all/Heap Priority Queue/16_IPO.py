import heapq
from typing import List

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        max_p = []
        min_c = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(min_c)

        for i in range(k):
            while min_c and min_c[0][0] <= w:
                c, p = heapq.heappop(min_c)
                heapq.heappush(max_p, -p)
            
            if not max_p:
                break
            
            w += -1*heapq.heappop(max_p)
        
        return w