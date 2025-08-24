from typing import List

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # DFS returns: total time needed to inform `node` (i.e., time from the head down to this node)
        def dfs(node):
            # If this node still has a manager (i.e., not computed/memoized yet)
            if manager[node] != -1:
                # Accumulate the time needed to inform this node:
                # it's the time to inform its manager (dfs(manager[node])) plus this node's own inform time.
                # We add the upstream time into informTime[node] to memoize the cumulative time to reach `node`.
                informTime[node] += dfs(manager[node])
                # Mark as memoized: set manager[node] = -1 so future calls know it's already computed
                manager[node] = -1
            # Now informTime[node] holds the total time from the head to this node.
            return informTime[node]

        res = 0
        # For every employee, compute how long it takes until they are informed,
        # and take the maximum (the company finishes when the slowest chain finishes).
        for node in range(n):
            res = max(res, dfs(node))
        return res
