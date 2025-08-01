class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:

        def sub(x):
            if x < 0:
                return 0
            
            l, cur, result = 0, 0, 0

            for  r in range(len(nums)):
                cur += nums[r]
                while cur > x:
                    cur -= nums[l]
                    l += 1
                result += (r-l+1)
            
            return result
            
        return sub(goal) - sub(goal-1)