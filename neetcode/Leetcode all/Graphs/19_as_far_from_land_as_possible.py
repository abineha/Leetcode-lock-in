from collections import deque
from typing import List

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        N = len(grid)
        q = deque()

        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    q.append([r, c])
        
        result = -1
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        while q:
            r, c = q.popleft()
            result = grid[r][c]

            for dr, dc in dirs:
                nr, nc = r+dr, c+dc

                if min(nr, nc) >= 0 and max(nr, nc) < N and grid[nr][nc] == 0:
                    q.append((nr, nc))
                    grid[nr][nc] = grid[r][c] +1
        
        return result-1 if result > 1 else -1