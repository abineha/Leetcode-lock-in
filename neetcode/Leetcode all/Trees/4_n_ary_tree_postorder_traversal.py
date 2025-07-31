# Definition for a Node.
from typing import Optional, List

class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        def recur(node):
            if not node:
                return 
            for c in node.children:
                recur(c)
            result.append(node.val)
        recur(root)
        return result
    
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        if not root:
            return result
        stack = [(root, False)]

        while stack:
            node, visited = stack.pop()
            if visited:
                result.append(node.val)
            else:
                stack.append((node, True))
                for c in node.children[::-1]:
                    stack.append((c, False))

        return result