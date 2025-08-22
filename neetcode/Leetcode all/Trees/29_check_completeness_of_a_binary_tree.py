from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        null = False
        q = deque([root])

        while q:
            node = q.popleft()
            if node:
                if null:    # encounter node after null
                    return False
                q.append(node.left)
                q.append(node.right)
            else:
                null = True
        
        return True
