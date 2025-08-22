from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 1
        q = deque([(root, 1)])

        while q:
            for i in range(len(q)):
                node, l = q.popleft()
                
                if node.left:
                    q.append((node.left, 2*l))
                if node.right:
                    q.append((node.right, 2*l+1))
            
            if len(q) > 1:
                result = max(result, q[-1][1] - q[0][1] + 1)
        
        return result