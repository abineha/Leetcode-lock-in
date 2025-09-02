from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def dfs(node, path, target):
            if not node:
                return ""
            if node.val == target:
                return "".join(path)
            
            path.append("L")
            result = dfs(node.left, path, target)
            if result:
                return result
            path.pop()

            path.append("R")
            result = dfs(node.right, path, target)
            if result:
                return result
            path.pop()

            return ""
        
        start_path = dfs(root, [], startValue)
        dest_path = dfs(root, [], destValue)
        i = 0

        while i < min(len(start_path), len(dest_path)):
            if start_path[i] != dest_path[i]:
                break
            i += 1
        
        result = ["U"] * len(start_path[i:]) + list(dest_path[i:])
        return "".join(result)
