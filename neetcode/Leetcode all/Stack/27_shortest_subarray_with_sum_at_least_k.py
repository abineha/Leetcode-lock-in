from collections import deque

class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        result = float('inf')  # stores the length of the shortest valid subarray found so far
        cur_sum = 0            # running prefix sum
        q = deque()            # stores (prefix_sum, index) in increasing order of prefix_sum

        for r in range(len(nums)):       # r = current right index of window
            cur_sum += nums[r]           # update prefix sum with current element

            # Case 1: subarray from 0 to r already satisfies sum >= k
            if cur_sum >= k:
                result = min(result, r + 1)  # length = r - (-1) → r+1

            # Case 2: shrink from the left while the condition holds
            # q[0] is the smallest index seen so far with smallest prefix sum
            while q and cur_sum - q[0][0] >= k:
                prefix, end_index = q.popleft()
                # Found subarray from end_index+1 to r with sum >= k
                result = min(result, r - end_index)

            # Maintain monotonic increasing prefix sums in deque
            # If current prefix sum is <= last in deque, pop last because
            # it will never give a shorter subarray in the future
            while q and q[-1][0] > cur_sum:
                q.pop()

            # Add current prefix sum with its index to deque
            q.append((cur_sum, r))
        
        # If result was never updated, return -1 (no valid subarray found)
        return -1 if result == float('inf') else result
