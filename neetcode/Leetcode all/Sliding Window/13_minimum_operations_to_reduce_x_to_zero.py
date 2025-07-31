class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        l, target = 0, sum(nums)-x
        cur_wind, max_wind = 0, -1

        for r in range(len(nums)):
            cur_wind += nums[r]
            while l <= r and cur_wind > target:
                cur_wind -= nums[l]
                l += 1
            if cur_wind == target:
                max_wind = max(max_wind, r-l+1)
        
        return -1 if max_wind == -1 else len(nums)-max_wind