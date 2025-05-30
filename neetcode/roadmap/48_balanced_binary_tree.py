from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if root is None:
                return [True, 0]    # it is balanced at h = 0
            
            L, R = dfs(root.left), dfs(root.right)
            balanced = L[0] and R[0] and abs(L[1] - R[1]) <=1 # L and R subtrees are balanced and height <=1

            return [balanced, 1 + max(L[1], R[1])]
        
        return dfs(root)[0]