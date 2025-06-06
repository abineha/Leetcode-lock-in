from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        q = deque()
        time, fresh = 0, 0
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for  c in range(COLS):
                if grid[r][c] == 1:     # Fresh oranges
                    fresh += 1
                if grid[r][c] == 2:     # rotten oranges
                    q.append([r,c])

        directions = [[1,0], [0,1], [-1,0], [0,-1]]

        while q and fresh > 0:
            for i in range(len(q)): 
                r, c = q.popleft()      # most recent
                for dr,dc in directions:
                    row, col = dr+r, dc+c
                    # if in bound and fresh make it rotten
                    if (row<0 or row==ROWS or col<0 or col==COLS or grid[row][col]!=1):
                        continue
                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1