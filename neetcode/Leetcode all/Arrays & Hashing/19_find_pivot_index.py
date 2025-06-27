class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        l = 0
        total = sum(nums)

        for i in range(len(nums)):
            r = total - l - nums[i]
            if l == r:
                return i
            l += nums[i]

        return -1        