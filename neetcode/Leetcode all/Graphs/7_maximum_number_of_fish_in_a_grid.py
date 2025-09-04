from typing import List

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            if (r<0 or c<0 or r == R or c == C or grid[r][c]==0 or (r,c) in visit):
                return 0

            visit.add((r, c))
            result = grid[r][c]
            neigh = [[r+1, c], [r-1, c], [r,c+1], [r,c-1]]

            for nr, nc in neigh:
                result += dfs(nr, nc)
            
            return result
        
        R, C = len(grid), len(grid[0])
        result = 0
        visit = set()

        for r in range(R):
            for c in range(C):
                result = max(result, dfs(r,c))
            
        return result