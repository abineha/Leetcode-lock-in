class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        map = {}
        for i in nums:
            map[i] = map.get(i, 0) + 1
        
        for i in map.values():
            if i%2 !=0:
                return False
        return True
        