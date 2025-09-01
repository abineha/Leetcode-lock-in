from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        result = None
        q = deque([(root, "")])

        while q:
            node, cur = q.popleft()
            cur = chr(ord('a')+node.val) + cur

            if not node.left and not node.right:
                result = min(result, cur) if result else cur

            if node.left:
                q.append((node.left, cur))
            
            if node.right:
                q.append((node.right, cur))
        
        return result