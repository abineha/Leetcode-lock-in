
# Definition for a Node.

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hashmap = {}    # old : new (nodes)

        def clone(node):    # dfs
            if node in hashmap:    # copy exists return new clone
                return hashmap[node]
            
            # create copy
            copy = Node(node.val)
            hashmap[node] = copy    # old : new (nodes)

            for neigh in node.neighbors:
                copy.neighbors.append( clone(neigh) )   # returns copy of the neighbor node
            return copy

        return clone(node) if node else None    # any node return its ok