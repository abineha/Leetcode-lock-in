from collections import Counter

class Solution:
    def findLucky(self, arr: list[int]) -> int:
        map = Counter(arr)
        result = -1

        for n in map:
            if n == map[n]:
                result = max(result, n)

        return result