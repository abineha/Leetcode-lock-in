from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        result = []
        q = deque([root])

        while q:
            lvl = []
            for i in range(len(q)):
                node = q.popleft()
                if node:    # avoids none next iter if below appended area none
                    lvl.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if lvl:
                result.append(lvl)
        return result