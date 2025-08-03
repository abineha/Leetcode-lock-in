class Solution:
    def minOperations(self, nums: list[int]) -> int:
        length = len(nums)
        nums = sorted(set(nums))
        r, result = 0, length

        for l in range(len(nums)):
            # nums[l] -> nums[l] + length - 1 + 1 if [1,5] make r stop at 6 (5+1)
            while r < len(nums) and nums[r] < nums[l] + length:
                r += 1
            window = (r-l)
            result = min(result, length - window)
        
        return result