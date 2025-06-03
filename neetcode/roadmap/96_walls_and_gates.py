from collections import deque

class Solution:
    def wallsAndGates(self, rooms: list[list[int]]) -> None:
        ROWS, COLS = len(rooms), len(rooms[0])
        visit = set()
        q = deque() 

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:    # finding all gates
                    q.append([r,c])
                    visit.add((r,c))

        def addroom(r, c):
            if r < 0 or r == ROWS or c < 0 or c == COLS or (r,c) in visit or rooms[r][c] == -1:
                return
            visit.add((r,c))
            q.append([r,c])

        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()  # BFS
                rooms[r][c] = dist  # for each gate

                addroom(r+1, c)
                addroom(r-1, c)
                addroom(r, c+1)
                addroom(r,c-1)
            dist += 1
