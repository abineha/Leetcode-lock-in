from typing import List 

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        R, C = len(grid1), len(grid1[0])
        visit = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r == R or c == C or (r, c) in visit or grid2[r][c] == 0:
                return True
                
            visit.add((r, c))
            result = grid1[r][c]

            result &= dfs(r, c-1)
            result &= dfs(r, c+1)
            result &= dfs(r+1, c)
            result &= dfs(r-1, c)

            return result
            
        count = 0

        for r in range(R):
            for c in range(C):
                if grid2[r][c] and (r, c) not in visit:
                    count += dfs(r, c)

        return count