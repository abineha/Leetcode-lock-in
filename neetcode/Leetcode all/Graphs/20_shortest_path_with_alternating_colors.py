from collections import defaultdict, deque
from typing import List

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = defaultdict(list)
        blue = defaultdict(list)

        for s, d in redEdges:
            red[s].append(d)

        for s, d in blueEdges:
            blue[s].append(d)
        
        answer = [-1 for i in range(n)]
        q = deque([(0, 0, None)])
        visit = set()
        visit.add((0, None))

        while q:
            node, l, col = q.popleft()

            if answer[node] == -1:
                answer[node] = l
            
            if col != "RED":
                for nei in red[node]:
                    if (nei, "RED") not in visit:
                        visit.add((nei, "RED"))
                        q.append([nei, l+1, "RED"])

            if col != "BLUE":
                for nei in blue[node]:
                    if (nei, "BLUE") not in visit:
                        visit.add((nei, "BLUE"))
                        q.append([nei, l+1, "BLUE"])
        
        return answer