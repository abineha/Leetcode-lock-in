from typing import List
import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        q = [(n, i) for i, n in enumerate(nums)]
        heapq.heapify(q)

        for i in range(k):
            n, i = heapq.heappop(q)
            nums[i] = n * multiplier
            heapq.heappush(q, (nums[i], i))
        
        return nums


