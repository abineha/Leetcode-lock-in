from typing import List

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            adj[u].append(v)

        # memo[u][v] = whether u can reach v
        memo = {}

        def dfs(u, target):
            if (u, target) in memo:
                return memo[(u, target)]

            if u == target:
                memo[(u, target)] = True
                return True

            for nei in adj[u]:
                if dfs(nei, target):
                    memo[(u, target)] = True
                    return True

            memo[(u, target)] = False
            return False

        res = []
        for u, v in queries:
            res.append(dfs(u, v))
        return res
