from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])  # always 1st val of preorder = root
        mid_index = inorder.index(preorder[0])  # L mid_index R = inorder
        root.left = self.buildTree(preorder[:mid_index + 1], inorder[: mid_index])
        root.right = self.buildTree(preorder[mid_index + 1 :], inorder[mid_index + 1 :])
        return