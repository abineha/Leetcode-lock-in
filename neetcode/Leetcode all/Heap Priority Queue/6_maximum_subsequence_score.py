from typing import List
import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pair = sorted(zip(nums1, nums2), key = lambda p: p[1], reverse = True)
        total = 0
        q = []
        result = 0

        for n1, n2 in pair:     # n2 contains min of k ele
            total += n1
            heapq.heappush(q, n1)

            if len(q) > k:
                total -= heapq.heappop(q)
            
            if len(q) == k:
                result = max(result, total * n2)
        
        return result