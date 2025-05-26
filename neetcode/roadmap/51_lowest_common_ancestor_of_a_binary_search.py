from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        while curr != None:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left    # both nodes are in the left subtree
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right   # both nodes are in the right subtree
            else:
                return curr         # split happens here, so this is the LCA