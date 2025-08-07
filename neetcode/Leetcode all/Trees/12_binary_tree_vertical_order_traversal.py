from collections import defaultdict, deque
# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = deque([(root, 0)])  # (node, column index)
        col_map = defaultdict(list)
        min_col, max_col = 0, 0

        while q:
            node, col_idx = q.popleft()
            min_col, max_col = min(min_col, col_idx), max(max_col, col_idx)
            
            col_map[col_idx].append(node.val)
            if node.left:
                q.append((node.left, col_idx-1))
            if node.right:
                q.append((node.right, col_idx+1))
            
        return [col_map[col] for col in range(min_col, max_col+1)]
