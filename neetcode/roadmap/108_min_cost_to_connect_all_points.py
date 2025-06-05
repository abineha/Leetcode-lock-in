import heapq

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        N = len(points)
        adj = {i:[] for i in range(N)}  # adjacency matric, i : list of [cost, node]

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):     # 1 point to others = combis
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dist,j])
                adj[j].append([dist, i])

        # PRIMS
        result = 0
        visit = set()
        minHeap = [[0,0]]   # [cost, point] - to minimise cost
        while len(visit) < N:
            cost, i = heapq.heappop(minHeap)
            if i in visit:
                continue
            visit.add(i)
            result += cost
            for neighCost, neigh in adj[i]:
                heapq.heappush(minHeap, [neighCost, neigh])

        return result