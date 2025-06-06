from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u, v, w in times:    # create an adjacency list
            edges[u].append((v, w))

        minHeap = [(0, k)] # starting dist = 0 for node k
        visit = set()
        t = 0 

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:     # loop 
                continue
            visit.add(n1)
            t = max(t, w1)

            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1+w2, n2))

        return  t if len(visit) == n else -1