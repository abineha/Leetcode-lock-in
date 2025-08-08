# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        result = []

        def preorder(root):
            if not root:
                return 
                
            result.append("(")
            result.append(str(root.val))

            if not root.left and root.right:
                result.append("()")

            preorder(root.left)
            preorder(root.right)
            
            result.append(")")

        preorder(root)
        return "".join(result)[1:-1]
