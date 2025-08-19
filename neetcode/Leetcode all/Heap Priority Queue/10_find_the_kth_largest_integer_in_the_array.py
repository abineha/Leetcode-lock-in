import heapq
from typing import List

class Num:
    def __init__(self, s):
        self.s = s
    
    def __lt__(self, o: "Num")-> bool:
        if len(self.s) != len(o.s):
            return len(self.s) < len(o.s)
        
        return self.s < o.s

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        q = []  # min heap

        for n in nums:
            heapq.heappush(q, Num(n))

            if len(q) > k :
                heapq.heappop(q)
        
        return q[0].s