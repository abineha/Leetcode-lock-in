from typing import List
import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        avail, pend = [], []

        for i, (eT, pT) in enumerate(tasks):
            heapq.heappush(pend, (eT, pT, i))
        
        t, result = 0, []

        while pend or avail:
            while pend and pend[0][0] <=t:
                eT, pT, i = heapq.heappop(pend)
                heapq.heappush(avail, (pT, i))
                
            if not avail:
                t = pend[0][0]
                continue
                
            pT, i = heapq.heappop(avail)    # processed the task with the smallest processing time
            t += pT
            result.append(i)
        
        return result