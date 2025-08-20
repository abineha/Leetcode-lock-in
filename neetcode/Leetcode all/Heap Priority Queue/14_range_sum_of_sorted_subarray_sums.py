import heapq
from typing import List

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10 ** 9 + 7
        sub_sum = []

        for i in range(n):
            cur = 0
            for j in range(i, n):
                cur = (cur +nums[j]) % MOD
                sub_sum.append(cur)
        
        sub_sum.sort()
        result = 0

        for i in range(left-1, right):
            result = (result + sub_sum[i]) % MOD
        
        return result
    
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10 ** 9 + 7
        
        # Step 1: Initialize a min-heap with tuples (value, index)
        # Each element is the subarray starting and ending at index i
        # Format: (current_subarray_sum, ending_index)
        q = [(val, i) for i, val in enumerate(nums)]
        heapq.heapify(q)  # Build the min-heap in O(n)

        result = 0

        # Step 2: Extract the smallest subarray sums in sorted order
        # We need sums from 1st to 'right'-th smallest
        for i in range(right):
            num, idx = heapq.heappop(q)  # Get the smallest subarray sum

            # If current subarray sum's order (i+1) is within [left, right],
            # add it to the result (modulo to avoid overflow)
            if i >= left - 1:
                result = (result + num) % MOD

            # Step 3: Generate the next subarray sum that starts at the same
            # starting point but extends to the next index
            # Example: if (sum of nums[i:j]) is taken, then push (nums[i:j+1])
            if idx + 1 < n:
                next_sum = (num + nums[idx+1], idx+1)
                heapq.heappush(q, next_sum)

        return result
