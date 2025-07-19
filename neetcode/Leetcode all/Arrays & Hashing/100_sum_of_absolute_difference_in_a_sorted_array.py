class Solution:
    def getSumAbsoluteDifferences(self, nums: list[int]) -> list[int]:
        total = sum(nums)
        left_sum = 0
        result = []

        for i, n in enumerate(nums):
            right_sum = total - left_sum - n
            result.append((i*n)-left_sum + right_sum-(len(nums)-i-1)*n)
            left_sum += n
        
        return result