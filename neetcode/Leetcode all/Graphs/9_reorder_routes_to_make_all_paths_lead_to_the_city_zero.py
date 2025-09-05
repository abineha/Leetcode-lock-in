from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = {(a, b) for a, b in connections}
        neigh = { city: [] for city in range(n)}
        visit = set()
        change = 0

        for a, b in connections:
            neigh[a].append(b)
            neigh[b].append(a)

        def dfs(city):
            nonlocal change
            visit.add(city)

            for n in neigh[city]:
                if n in visit:
                    continue
                if (n, city) not in edges:
                    change += 1
                dfs(n)
        
        dfs(0)
        return change