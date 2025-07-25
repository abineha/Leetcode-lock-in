class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        l, r = 0, len(nums) - 1
        result = []

        while l <= r:
            if nums[r]**2 > nums[l]**2:
                result.append(nums[r]**2)
                r -= 1
            else:
                result.append(nums[l]**2)
                l+=1
        
        return result[::-1]