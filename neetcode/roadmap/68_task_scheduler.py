from collections import deque, Counter
import heapq

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        # each task = 1 unit
        # min(idle time)

        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]   # hashmap of letter : 
        heapq.heapify(maxHeap)   #order it

        t = 0
        q = deque()   # [count, ready]

        while maxHeap or q :
            t += 1

            if maxHeap:
                count = heapq.heappop(maxHeap) + 1   # proccessed -ve val
                if count:
                    q.append([count, t + n])
            
            # check if any task is ready to be re-aded to heap
            if q and q[0][1] == t:
                heapq.heappush(maxHeap, q.popleft()[0])
        return t