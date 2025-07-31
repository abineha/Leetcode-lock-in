from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l, result = 0, 0
        map = defaultdict(int)

        for r in range(len(s)):
            map[s[r]] += 1
            while len(map) == 3:
                result += (len(s) - r)
                map[s[l]] -= 1
                if map[s[l]] == 0:
                    map.pop(s[l])
                l += 1
        
        return result
    
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l, result = 0, 0
        map = [0, 0, 0]

        for r in range(len(s)):
            map[ord(s[r])- ord('a')] += 1
            while map[0] and map[1] and map[2]:
                result += (len(s) - r)
                map[ord(s[l])- ord('a')] -= 1
                l += 1
                
        return result