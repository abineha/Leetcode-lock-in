from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder(node):
            if not node:
                return None
            
            inorder(node.left)
            result.append(node)
            inorder(node.right)
        
        result = []
        inorder(root)
        node1, node2 = None, None

        for i in range(len(result)-1):
            if result[i].val > result[i+1].val:
                node2 = result[i+1]
                if node1 is None:
                    node1 = result[i]
                else:
                    break
        
        node1.val, node2.val = node2.val, node1.val
            
