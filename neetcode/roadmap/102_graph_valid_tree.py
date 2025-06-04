class SOlution:
    def validTree(self, n, edges):
        if not n:   # empty graph
            return True
        
        adj = {i:[] for i in range(n)}  # adjacency matrix
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        visit = set()

        def dfs(i, prev):
            if i in visit:  # loop
                return False
            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j,i):    ## loop
                    return False
            return True
        
        return dfs(0, -1) and len(visit) == n