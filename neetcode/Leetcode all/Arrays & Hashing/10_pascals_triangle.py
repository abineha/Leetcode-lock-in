class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result = [ [1] ]

        for i in range(numRows - 1):
            temp = [0] + result[-1] + [0]
            row = []
            for j in range(len(result[-1]) + 1):
                row.append(temp[j]+temp[j+1])
            result.append(row)
        return result
        

# DP
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = [[1] * (i + 1) for i in range(numRows)]
        for i in range(2, numRows):
            for j in range(1, i):
                res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
        return res


