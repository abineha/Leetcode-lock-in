class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        l, r = 0, sum(nums)
        result = 0

        for i in range(len(nums)-1):
            l += nums[i]
            r -= nums[i]

            if l >= r:
                result += 1
        
        return result