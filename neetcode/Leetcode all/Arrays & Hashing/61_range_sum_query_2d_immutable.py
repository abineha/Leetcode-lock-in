class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        row, col = len(matrix), len(matrix[0])
        self.sumMatrix = [[0]*(col+1) for i in range(row+1)]
        for r in range(row):
            prefix = 0
            for c in range(col):
                prefix += matrix[r][c]
                self.sumMatrix[r+1][c+1] = prefix + self.sumMatrix[r][c+1]



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, r2, c1, c2 = row1+1, row2+1, col1+1, col2+1
        full_area = self.sumMatrix[r2][c2]
        top_area = self.sumMatrix[r1-1][c2]
        left_area = self.sumMatrix[r2][c1-1]
        repeated_square = self.sumMatrix[r1-1][c1-1]
        return full_area - top_area - left_area + repeated_square

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)