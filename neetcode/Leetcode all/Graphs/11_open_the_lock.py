from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        
        q = deque([["0000", 0]])    # [lock, turns]
        visit = set(deadends)

        def children(lock):
            result = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)   # rotate up
                result.append(lock[:i] + digit + lock[i+1:])
                digit = str((int(lock[i]) - 1 + 10) % 10)  # rotate down
                result.append(lock[:i] + digit + lock[i+1:])
            return result
        
        while q:
            lock, turn = q.popleft()

            if lock == target:
                return turn
            
            for child in children(lock):
                if child not in visit:
                    visit.add(child)
                    q.append([child, turn + 1])
        
        return -1
