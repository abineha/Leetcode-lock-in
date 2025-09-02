from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.cur_sum = 0

        def dfs(node):
            if not node:
                return
            
            dfs(node.right)
            temp = node.val
            node.val += self.cur_sum
            self.cur_sum += temp
            dfs(node.left)

        dfs(root)
        return root