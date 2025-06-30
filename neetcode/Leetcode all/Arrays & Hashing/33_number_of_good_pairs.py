class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        result = 0
        map = {} 
        for n in nums:
            result += map.get(n, 0)
            map[n] = map.get(n, 0) + 1
        return result