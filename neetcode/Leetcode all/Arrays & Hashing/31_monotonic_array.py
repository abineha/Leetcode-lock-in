class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        inc, dec = True, True

        for i in range(len(nums)-1):
            if not(nums[i] <= nums[i+1]):
                inc = False
            if not(nums[i] >= nums[i+1]):
                dec = False

        return inc or dec        