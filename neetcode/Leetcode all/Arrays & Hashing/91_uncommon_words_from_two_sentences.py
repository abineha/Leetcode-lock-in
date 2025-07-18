from collections import defaultdict

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        map = defaultdict(int)

        for w in s1.split(" ")+s2.split(" "):
            map[w] += 1
        
        result = []

        for w, cnt in map.items():
            if cnt == 1:
                result.append(w)
        
        return result
        