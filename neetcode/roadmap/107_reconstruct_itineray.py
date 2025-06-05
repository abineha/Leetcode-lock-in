from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        adj = defaultdict(list)
        
        # Sort in reverse lexicographical order so we can pop the smallest later
        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)
        
        result = []
        
        def dfs(src):
            while adj[src]:
                next_dst = adj[src].pop()
                dfs(next_dst)
            result.append(src)
        
        dfs("JFK")
        return result[::-1]  # reverse at the end
