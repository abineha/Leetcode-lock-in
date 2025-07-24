class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        result = count = 0

        for n in nums:
            if n==1:
                count += 1
            else:
                result = max(count, result)
                count = 0
        
        return max(result, count)        