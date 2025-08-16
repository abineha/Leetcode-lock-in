from typing import Optional

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        num = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            num.append(node.val)
            dfs(node.right)

        dfs(root)        
        result = num[1] - num[0]

        for i in range(2, len(num)):
            result = min(result, num[i]-num[i-1])
        
        return result