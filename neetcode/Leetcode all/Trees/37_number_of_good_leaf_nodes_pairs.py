from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        self.pair = 0

        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [1]
            
            l_dist = dfs(node.left)
            r_dist = dfs(node.right)

            for d1 in l_dist:
                for d2 in r_dist:
                    if d1+d2 <= distance:
                        self.pair += 1
            
            all_dist = l_dist + r_dist
            return [d+1 for d in all_dist]
        
        dfs(root)
        return self.pair