from collections import defaultdict, deque
from typing import List

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        adj = defaultdict(list)

        for i, dst in enumerate(edges):
            adj[i].append(dst)
        
        def bfs(src, dist_map):
            q = deque()
            q.append([src, 0])
            dist_map[src] = 0

            while q:
                node, d = q.popleft()

                for n in adj[node]:
                    if n not in dist_map:
                        q.append([n, d+1])
                        dist_map[n] = d+1
        
        dist1, dist2 = {}, {}
        bfs(node1, dist1)
        bfs(node2, dist2)

        result = -1
        result_dist = float('inf')

        for i in range(len(edges)):
            if i in dist1 and i in dist2:
                dist = max(dist1[i], dist2[i])

                if dist < result_dist:
                    result = i
                    result_dist = dist
        
        return result