class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        result = max(nums)  # 0 not a good default val if [-1]
        curMin, curMax = 1, 1   # neutral values

        for n in nums:
            if n == 0:  # neutralise
                curMax, curMin = 1, 1   # reset
                continue
             
            temp = curMax * n
            curMax = max(curMax * n, curMin * n, n) # [-1, 8]
            curMin = min(temp, curMin * n, n)       # [-1,-8]
            
            result = max(curMax, result)

        return result