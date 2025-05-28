class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        
        R, C = len(board), len(board[0])
        path = set() # avoid same ele into consideration

        def dfs(r, c, i):
            if i == len(word):
                return True        
            if (r < 0 or c < 0 or r > R or c > C or word[i] != board[r][c] or (r, c) in path):
                return False
            
            path.add((r, c))    # found the char we need
            result = (dfs(r + 1, c, i + 1) or
                      dfs(r - 1, c, i + 1) or
                      dfs(r, c + 1, i + 1) or
                      dfs(r, c - 1, i + 1) 
                     )
            
            path.remove((r, c))    # undo / backtrack
            return result
    
        for r in range(R):
            for c in range(C):
                if dfs(r, c, 0):
                    return True
        return False