class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        result = len(nums)      # n value

        for i in range(len(nums)):
            result += (i - nums[i])     # [0, len(n) - 1]

        return result