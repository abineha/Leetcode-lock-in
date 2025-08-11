import math

class Solution:
    def minimumSize(self, nums: list[int], maxOperations: int) -> int:
        def valid(x):
            op = 0
            for i in nums:
                op += math.ceil(i/x) - 1
                if op > maxOperations:
                    return False
            return True
        
        l, r = 1, max(nums)
        result = 0

        while l <= r:
            m = (l+r) // 2
            if valid(m):
                r = m-1
                result = m
            else:
                l = m+1
        
        return result