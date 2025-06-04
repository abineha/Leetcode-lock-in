class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1]* n
        
        def find(n1):   # find it root parent of a chain
            result = n1
            while result != parent[result]:     # path compression
                parent[result] = parent[parent[result]]     # path compression, parent of result = its grandparent
                result = parent[result]
            return result

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:    # did not do a union, already a chain
                return 0
            if rank[p2] > rank[p1]:     # longer chain = parent
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            return 1
        
        result = n
        for n1, n2 in edges:
            result -= union(n1, n2)
        
        return result