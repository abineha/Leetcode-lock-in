from typing import List
import heapq

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d = {}

        for i in arr:
            d[i] = d.get(i, 0) + 1
        
        q = list(d.values())
        heapq.heapify(q)
        result = len(q)

        while k > 0 and q:
            f = heapq.heappop(q)

            if k >= f:
                k -= f
                result -= 1
        
        return result