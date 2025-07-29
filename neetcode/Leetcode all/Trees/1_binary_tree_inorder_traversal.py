# Definition for a binary tree node.

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def recur(root):
            if not root:    # null
                return
            
            recur(root.left)    # left subtree
            result.append(root.val)
            recur(root.right)   # right subtree
        
        recur(root)
        return result

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            result.append(cur.val)
            cur = cur.right
        
        return result

# Call: recur(1)
#   → recur(1.left) → None → return
#   → result.append(1)
#   → recur(1.right) → recur(2)
#        → recur(2.left) → recur(3)
#             → recur(3.left) → None → return
#             → result.append(3)
#             → recur(3.right) → None → return
#        → result.append(2)
#        → recur(2.right) → None → return

# Initial:

# stack = [], cur = 1
# Push 1 → go left → cur = None

# stack = [1]
# Pop 1 → append 1 → go right → cur = 2
# result = [1]
# Push 2 → go left → cur = 3

# stack = [2, 3]
# Push 3 → go left → cur = None

# stack = [2, 3]
# Pop 3 → append 3 → cur = None
# result = [1, 3]
# Pop 2 → append 2 → cur = None
# result = [1, 3, 2]

# Final result = [1, 3, 2]