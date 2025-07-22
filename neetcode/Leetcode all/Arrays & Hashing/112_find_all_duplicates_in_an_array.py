class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        result = []
        for n in nums:
            n = abs(n)

            if nums[n-1] < 0:
                result.append(n)

            nums[n-1] = -nums[n-1]
        
        return result