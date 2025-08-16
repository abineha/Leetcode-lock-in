from typing import Optional
from collections import deque
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        q = deque([(root.left, root.right)])

        while q:
            for i in range(len(q)):
                l, r = q.popleft()

                if not l and not r:
                    continue
                if not l or not r or l.val != r.val:
                    return False
                
                q.append((l.left, r.right))
                q.append((l.right, r.left))
        
        return True