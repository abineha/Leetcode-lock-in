class Solution:
    def arraySign(self, nums: list[int]) -> int:
        sign = 1
        
        for n in nums:
            if n == 0:
                return 0
            if n < 0:
                sign *= -1
        
        return sign