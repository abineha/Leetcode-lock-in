from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        q = deque([root])

        while q:
            large = q[0].val

            for i in range(len(q)):
                ele = q.popleft()
                large = max(large, ele.val)

                if ele.left:
                    q.append(ele.left)
                if ele.right:
                    q.append(ele.right)
            
            result.append(large)
        
        return result
