import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        map = Counter(s)
        q = [ (-f, c) for c, f in map.items()]
        heapq.heapify(q)
        prev = (0, "")
        result = []

        while q:
            f, c = heapq.heappop(q)
            result.append(c)

            if prev[0] < 0:
                heapq.heappush(q, prev)
            
            prev = (f+1, c)
        
        result = "".join(result)

        if len(result) != len(s):
            return ""

        return result