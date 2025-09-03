from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        
        r, c = len(image), len(image[0])
        dir = [1, 0, -1, 0, 1]

        def dfs(i, j, col):
            if not (0 <= i < r) or not (0 <= j < c) or image[i][j] != col:
                return
            
            image[i][j] = color

            for d in range(4):
                dfs(i + dir[d], j + dir[d+1], col)
        
        dfs(sr, sc, image[sr][sc])
        return image