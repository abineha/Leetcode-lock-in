from typing import List 

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = {}
        result = []

        def dfs(i):
            if i in safe:
                return safe[i]
            
            safe[i] = False     # assume

            for n in graph[i]:     # neighbors
                if not dfs(n):
                    return False
            
            safe[i] = True
            return True
        
        for i in range(n):
            if dfs(i):
                result.append(i)
        
        return result