class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        nums.sort()
        result = 0
        r = len(nums)-1
        mod = 10**9 + 7

        for i, left in enumerate(nums):
            while left + nums[r] > target and i <= r:
                r -= 1
            if i <= r:
                result += (2**(r-i))
                result %= mod
        
        return result