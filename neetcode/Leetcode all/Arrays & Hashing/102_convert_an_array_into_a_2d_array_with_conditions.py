from collections import defaultdict

class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        map = defaultdict(int)
        result = []

        for n in nums:
            row = map[n]
            if len(result) == row:
                result.append([])
            
            result[row].append(n)
            map[n] += 1
        
        return result
        