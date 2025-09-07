from typing import List

class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        R, C = len(board), len(board[0])
        dirs = [[1, 0], [-1, 0], [1, 1], [1, -1], [0, 1], [0, -1], [-1, -1], [-1, 1]] 

        def legal(row, col, color, d):
            dr, dc = d
            row, col = row+dr, col+dc
            length = 1

            while(0 <= row < R and 0 <= col < C):
                length += 1

                if board[row][col] == ".":
                    return False
                
                if board[row][col] == color:
                    return length >= 3
                
                row, col = row+dr, col+dc
            
            return False
        
        for d in dirs:
            if legal(rMove, cMove, color, d):
                return True
        
        return False