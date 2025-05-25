from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive DFS

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        return 1 + max(self.maxDepth(root.left), (self.maxDepth(root.right)))
    
# BFS

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        q = deque([root])
        lvl = 0

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            lvl += 1

        return lvl
    
# iterative dfs
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        result = 0
        stack = [[root, 1]]

        while stack:
            node, depth = stack.pop()

            if node:
                result = max(result, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])

        return result