# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def recur(root):
            if not root:
                return
            recur(root.left)
            recur(root.right)
            result.append(root.val)            
        
        recur(root)
        return result
    
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, visited = [root], [False]
        result = []

        while stack:
            cur, v = stack.pop(), visited.pop()
            if cur:
                if v:
                    result.append(cur.val)
                else:
                    stack.append(cur)
                    visited.append(True) 
                    stack.append(cur.right)
                    visited.append(False) 
                    stack.append(cur.left)
                    visited.append(False)                      


        return result