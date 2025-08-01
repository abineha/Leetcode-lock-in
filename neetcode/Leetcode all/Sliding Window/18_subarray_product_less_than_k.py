class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        l, result = 0, 0
        product = 1

        for r in range(len(nums)):
            product *= nums[r]
            
            while l <= r and product >= k:
                product //= nums[l]
                l += 1

            result += (r-l+1)
        
        return result