class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        map = {}

        for n in arr1:
            map[n] = map.get(n, 0) + 1
        
        result = []

        for n in arr2:
            result += [n] * map.pop(n)

        for n in sorted(map):
            result += [n] * map[n]
        
        return result