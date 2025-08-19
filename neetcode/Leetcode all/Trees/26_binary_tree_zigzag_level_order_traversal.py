from typing import List
from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        q = deque([root] if root else [])
        L = True

        while q:
            lvl = []
            for i in range(len(q)):
                node = q.popleft()
                lvl.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if not L:
                lvl.reverse()
            
            result.append(lvl)
            L = not L
        
        return result

                    

