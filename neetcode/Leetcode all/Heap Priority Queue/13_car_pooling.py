import heapq
from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t:t[1])
        q = []
        cur = 0

        for num, start, end in trips:
            while q and q[0][0] <= start:
                cur -= heapq.heappop(q)[1]
            
            cur += num

            if cur > capacity:
                return False
            
            heapq.heappush(q, [end, num])
        
        return True