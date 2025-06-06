class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])

        # 1. capture unsurrounded regions, borders  ( O -> T )   [ DFS ]
        def capture(r,c):
            if r<0 or c<0 or r==ROWS or c==COLS or board[r][c]!="O":
                return
            board[r][c] = "T"
            capture(r+1,c)
            capture(r-1,c)
            capture(r,c+1)
            capture(r,c-1)
            
        # border
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r in [0,ROWS-1] or c in [0, COLS-1]):
                    capture(r,c)

        # 2. Capture the surrounded region ( O -> X )
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]=="O":
                    board[r][c] = "X"
        
        # 3. uncapture the unsurrounded regions ( T -> O )
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
