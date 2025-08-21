import heapq
from typing import List

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        result = nums[0]
        max_q = [(-nums[0], 0)]  # (max_sum, idx)

        for i in range(1, len(nums)):
            while i - max_q[0][1] > k:
                heapq.heappop(max_q)
            
            cur_max = max(nums[i], nums[i] - max_q[0][0])
            result = max(result, cur_max)
            heapq.heappush(max_q, (-cur_max, i))
        
        return result



