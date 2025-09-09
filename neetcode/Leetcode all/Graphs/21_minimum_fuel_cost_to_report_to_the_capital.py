from collections import defaultdict
from math import ceil   
from typing import List

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        adj = defaultdict(list)

        for s, d in roads:
            adj[s].append(d)
            adj[d].append(s)
        
        def dfs(node, parent):
            nonlocal result
            ppl = 0

            for c in adj[node]:
                if c != parent:
                    p = dfs(c, node)
                    ppl += p
                    result += int(ceil(p/seats))
            
            return ppl + 1
        
        result = 0
        dfs(0, -1)
        return result