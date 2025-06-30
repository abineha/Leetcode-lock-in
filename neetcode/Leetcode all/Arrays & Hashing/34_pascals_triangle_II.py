class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        l = [1]
        for i in range(rowIndex):
            l = [0] + l + [0]
            temp = []
            for j in range(len(l) - 1):
                temp.append(l[j] + l[j+1])
            l = temp
        return l
