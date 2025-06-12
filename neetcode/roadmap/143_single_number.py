class Solution:
    def singleNumber(self, nums: list[int]) -> int:                
        result = 0  # n ^ 0 = n
        for n in nums:
            result = result ^ n
        return result