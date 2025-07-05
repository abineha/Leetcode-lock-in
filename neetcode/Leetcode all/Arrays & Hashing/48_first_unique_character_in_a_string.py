class Solution:
    def firstUniqChar(self, s: str) -> int:
        map = {}
        n = len(s)
        result = n

        for i, c in enumerate(s):
            if map.get(c, -1) == -1:
                map[c] = i
            else:
                map[c] = n
        
        for i in map:
            result = min(result, map[i])
        
        return -1 if result == n else result
        