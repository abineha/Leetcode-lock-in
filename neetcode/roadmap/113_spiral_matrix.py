class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []
        l, r = 0, len(matrix[0])
        top, bot = 0, len(matrix)

        while l < r and top < bot:
            # L -> R get i in top row
            for i in range(l,r):
                result.append(matrix[top][i])
            # top over so shift
            top += 1
            # T -> B get i in right col
            for i in range(top, bot):
                result.append(matrix[i][r-1])   # right is 1 more than index pos
            # right over so shift
            r -= 1
            # check bounds
            if not(l<r and top<bot):
                break
            # R -> L bottom row in reverse
            for i in range(r-1, l-1, -1):
                result.append(matrix[bot-1][i])
            # bottom over so shift
            bot -= 1
            # B -> T get i in left col in reverse
            for i in range(bot-1, top-1, -1):
                result.append(matrix[i][l])
            #left over so shift
            l += 1
        
        return result