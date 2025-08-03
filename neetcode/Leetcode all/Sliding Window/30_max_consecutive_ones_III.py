class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        l, result = 0, 0
        num_zeros = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                num_zeros += 1
            
            if num_zeros > k:
                if nums[l] == 0:
                    num_zeros -= 1
                l += 1

            result = max(result, (r-l+1))
        
        return result