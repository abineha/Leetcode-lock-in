from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, L, R):
            if not node:
                return True # is a BST
            if not (node.val > L and node.val < R):
                return False
            return (valid(node.left,L, node.val) and valid(node.right, node.val, R))
            
        return valid(root, float("-inf"), float("inf"))
    