class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        N = len(edges)
        parent = [i for i in range(N+1)]    # ith node -> parent (1-n), parent of itself
        rank = [1]*(N+1)

        def find(n):
            if n!=parent[n]:    # not a parent of itself
                parent[n] = find(parent[n])     # goes to root parent node
            return parent[n]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False    # cycle
            if rank[p1] > rank[p2]:
                parent[p2] = p1     # update parent
                rank[p1] += p2
            else:
                parent[p1] = p2
                rank[p2] += p1
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]