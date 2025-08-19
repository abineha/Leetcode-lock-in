import heapq
from typing import List

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        result = [0] * len(tasks)
        avail = [(servers[i], i) for i in range(len(servers))]
        heapq.heapify(avail)
        unavail = []
        t = 0

        for i in range(len(tasks)):
            t = max(t, i)

            if len(avail) == 0: # no servers available 
                t = unavail[0][0]   # set t to top of minheap containing time it finishes in unavail heap
            
            while unavail and unavail[0][0] <= t:
                time, serv_weight, idx = heapq.heappop (unavail)    # finish processing top of min heap
                heapq.heappush(avail, (serv_weight, idx))

            # there is server in avail, so assign
            w, idx = heapq.heappop(avail)
            result[i] = idx
            heapq.heappush(unavail, (t+tasks[i], w, idx))

        return result                        
