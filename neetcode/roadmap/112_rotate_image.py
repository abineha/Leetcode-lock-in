class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix)-1

        while l < r:
            for  i in range(r-l):      # except last ele (n-1) rotations
                top, bot = l, r
                # save topLeft ele
                topLeft = matrix[top][l+i]
                # move bot left -> top left
                matrix[top][l+i] = matrix[bot-i][l]
                # move bot right -> bot left
                matrix[bot-i][l] = matrix[bot][r-i]
                # move top right -> bot right
                matrix[bot][r-i] = matrix[top+i][r]
                # move topLeft -> top right
                matrix[top+i][r] = topLeft
            r-=1
            l+=1