from collections import deque
from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length = len(board)
        board.reverse()

        def pos(square):
            r = (square-1) // length
            c = (square-1) % length

            if r % 2:
                c = length - c - 1
            
            return [r, c]

        q = deque([[1, 0]])
        visit = set()

        while q:
            square, move = q.popleft()
            
            for i in range(1, 7):
                nexts = square + i
                r, c = pos(nexts)

                if board[r][c] != -1:
                    nexts = board[r][c]
                if nexts == length*length:
                    return move + 1
                if nexts not in visit:
                    visit.add(nexts)
                    q.append([nexts, move+1])

        return -1