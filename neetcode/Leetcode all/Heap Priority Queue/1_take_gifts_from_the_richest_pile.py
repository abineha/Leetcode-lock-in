import heapq
from math import sqrt, floor
from typing import List

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(len(gifts)):
            gifts[i] = -gifts[i]

        heapq.heapify(gifts)

        for i in range(k):
            n = -heapq.heappop(gifts)
            heapq.heappush(gifts, -floor(sqrt(n)))
        
        return -sum(gifts)