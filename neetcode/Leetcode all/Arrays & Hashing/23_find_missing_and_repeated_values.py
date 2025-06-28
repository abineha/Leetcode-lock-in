from collections import defaultdict

class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        N = len(grid)
        map = defaultdict(int)

        for i in range(N):
            for j in range(N):
                map[grid[i][j]] +=  1

        doubl = miss = 0
        for num in range(1, N*N + 1):
            if map[num] == 0:
                miss = num
            if map[num] == 2:
                doubl = num
        
        return [doubl, miss]