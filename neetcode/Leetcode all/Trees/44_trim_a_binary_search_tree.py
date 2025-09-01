from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        while root and (root.val < low or root.val > high):
            root = root.right if root.val < low else root.left
        
        temp = root

        while root:
            while root.left and root.left.val < low:
                root.left = root.left.right
            
            root = root.left
        
        root = temp

        while root:
            while root.right and root.right.val > high:
                root.right = root.right.left
            
            root = root.right

        return temp