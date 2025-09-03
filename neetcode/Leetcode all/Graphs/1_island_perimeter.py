from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        visit = set()

        def dfs(i, j):
            if (i, j) in visit:
                return 0
            if i < 0 or j < 0 or i >= r or j >= c or grid[i][j] == 0:
                return 1
            
            visit.add((i, j))
            peri = dfs(i, j+1) + dfs(i+1, j) + dfs(i, j-1) + dfs(i-1, j)
            
            return peri
        
        for i in range(r):
            for j in range(c):
                if grid[i][j]:
                    return dfs(i,j)
        
        return 0