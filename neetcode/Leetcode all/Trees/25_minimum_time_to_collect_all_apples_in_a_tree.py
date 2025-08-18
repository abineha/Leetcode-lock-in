from typing import List

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        def dfs(cur, p):
            t = 0

            for c in adj[cur]:
                if c == p:
                    continue
                
                c_time = dfs(c, cur)

                if c_time or hasApple[c]:
                    t += 2 + c_time
            return t

        adj = {i : [] for i in range(n)}
        
        for p, c in edges:
            adj[p].append(c)
            adj[c].append(p)
        
        return dfs(0, -1)