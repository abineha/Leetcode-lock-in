from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        result = 0
        r, c = len(grid), len(grid[0])
        r_count, c_count = [0]*r, [0]*c

        for ri in range(r):
            for ci in range(c):
                if grid[ri][ci] == 1:
                    r_count += 1
                    c_count += 1
        
        for ri in range(r):
            for ci in range(c):
                if grid[ri][ci] and r_count > 1 or c_count > 1:
                    result += 1
        
        return result