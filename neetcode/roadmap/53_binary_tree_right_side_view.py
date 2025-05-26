from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        result = []
        q = deque([root])

        while q:
            R = None
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    R = node
                    q.append(node.left)
                    q.append(node.right)
            if R:    
                result.append(R.val)
        return result