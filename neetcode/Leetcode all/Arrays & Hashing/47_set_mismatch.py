class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        sum = (n * (n+1) ) / 2
        map = {}

        for i in nums:
            if map.get(i, -1) == -1:
                map[i] = 1
                sum -= i
            else:
                twice = i
        
        return [twice, int(sum)]