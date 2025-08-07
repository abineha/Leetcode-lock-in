class Solution:
    def maxWidthRamp(self, nums: list[int]) -> int:
        max_right = [0] * len(nums)
        i, prev_max = len(nums)-1, 0

        for n in reversed(nums):
            max_right[i] = max(prev_max, n)
            prev_max = max_right[i]
            i -= 1
        
        result, L = 0, 0

        for R in range(len(nums)):
            while nums[L] > max_right[R]:
                L += 1
            result = max(result, R-L)

        return result