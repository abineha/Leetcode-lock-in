from collections import defaultdict
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        count = defaultdict(int)
        odd = 0

        def dfs(cur):
            nonlocal odd

            if not cur:
                return 0
            
            count[cur.val] += 1
            odd_change = 1 if count[cur.val] % 2 == 1 else -1
            odd += odd_change

            if not cur.left and not cur.right:
                result = 1 if odd <= 1 else 0
            else:
                result = dfs(cur.left) + dfs(cur.right)
            
            odd -= odd_change
            count[cur.val] -= 1
            return result
        
        return dfs(root)