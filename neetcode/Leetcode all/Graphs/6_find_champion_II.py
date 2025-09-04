from typing import List

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        incoming = [0] * n 
        champ = []

        for s, d in edges:
            incoming[d] += 1
        
        for i, c in enumerate(incoming):
            if not c:
                champ.append(i)

        if len(champ) > 1:
            return -1
        
        return champ[0]