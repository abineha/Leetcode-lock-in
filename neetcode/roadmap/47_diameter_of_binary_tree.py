from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0

        def dfs(node):      # height of node in tree
            if node == None:
                return 0
            
            L = dfs(node.left)
            R = dfs(node.right)

            self.result = max(self.result, L + R)
            return 1 + max(L, R)
        
        dfs(root)
        return self.result
