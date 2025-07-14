class Solution:
    def gridGame(self, grid: list[list[int]]) -> int:
        N =  len(grid[0])
        result = float("inf")
        preRow1, preRow2 = grid[0].copy(), grid[1].copy()

        for i in range(1, N):
            preRow1[i] += preRow1[i-1]
            preRow2[i] += preRow2[i-1]

        for i in range(N):
            top = preRow1[-1] - preRow1[i]
            bottom = preRow2[i-1] if i > 0 else 0
            secondRobo = max(top, bottom)
            result = min(result, secondRobo)

        return result        