from collections import defaultdict
from typing import List

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)

        for s, d, dist in roads:
            adj[s].append((d, dist))
            adj[d].append((s, dist))

        def dfs(i):
            if i in visit:
                return
            
            visit.add(i)
            nonlocal result

            for nei, dist in adj[i]:
                result = min(result, dist)
                dfs(nei)
        
        result = float('inf')
        visit = set()
        dfs(1)
        return result