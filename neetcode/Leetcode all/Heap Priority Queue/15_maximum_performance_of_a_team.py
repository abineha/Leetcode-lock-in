import heapq
from typing import List

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        eng = []

        for e, s in zip(efficiency, speed):
            eng.append([e, s])
        
        eng.sort(reverse = True)
        result, speed = 0, 0
        q = []

        for e, s in eng:
            if len(q) == k:
                speed -= heapq.heappop(q)

            speed += s
            heapq.heappush(q, s)
            result = max(result, e*speed)

        return result % (10**9 + 7)