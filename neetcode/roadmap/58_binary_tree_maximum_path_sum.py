from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = [root.val]

        # return max path sum WITHOUT split
        def dfs(root):
            if not root:
                return 0

            L_max = dfs(root.left)  # recursively considers left subtree down -> up
            R_max = dfs(root.right)

            L_max = max(L_max, 0)  # take 0 if -ve ignore node
            R_max = max(R_max, 0)  # take 0 if -ve ignore node

            # max path sum with split / \ 
            result[0] = max(result[0], root.val + L_max + R_max)  # if split greater than result update

            return root.val + max(L_max, R_max)  # return max sum WITHOUT SPLIT
        
        dfs(root)
        return result[0]