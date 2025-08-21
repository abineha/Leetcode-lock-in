from collections import defaultdict
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        map = defaultdict(list)

        def dfs(node):
            if not node:
                return "null"
            
            s = ",".join([str(node.val), dfs(node.left), dfs(node.right)])

            if len(map[s]) == 1:
                result.append(node)
            
            map[s].append(node)
            return s 
        
        result = []
        dfs(root)
        return result