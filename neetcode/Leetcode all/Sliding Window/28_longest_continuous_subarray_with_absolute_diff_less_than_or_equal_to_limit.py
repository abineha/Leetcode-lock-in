from collections import deque

class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        min_q = deque()     # mono inc
        max_q = deque()     # mono dec
        l, result = 0, 0

        for r in range(len(nums)):
            while min_q and nums[r] < min_q[-1]:
                min_q.pop()
            while max_q and nums[r] > max_q[-1]:
                max_q.pop()
            
            min_q.append(nums[r])
            max_q.append(nums[r])

            while max_q[0] - min_q[0] > limit:
                if nums[l] == max_q[0]:
                    max_q.popleft()
                if nums[l] == min_q[0]:
                    min_q.popleft()
                l += 1
            
            result = max(result, r-l+1)
        
        return result
    
# Window: [1, 3, 3, 5]
# max_q: [5, 3, 3, 3] ← front is 5
# → As we slide left, 1 is removed
# → Then 3 is removed → it’s min_q[0] → popped
# → Eventually 5 is removed → if it's max_q[0], popped


# We’re not tracking all elements. we’re tracking candidates for max/min.
# Once an element slides out of the window and reaches the front, we pop it.
# If it’s in the middle or back, it’s fine. we’ll never use it for current window’s max/min.

