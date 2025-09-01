from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}
        def backtrack(n):
            if n == 0:
                return []
            if n == 1:
                return [TreeNode()]
            if n in memo:
                return memo[n]
            
            result = []

            for l in range(n):
                r = n-l-1
                l_tree = backtrack(l)
                r_tree = backtrack(r)

                for t1 in l_tree:
                    for t2 in r_tree:
                        result.append(TreeNode(0, t1, t2))

            memo[n] = result
            return result

        return backtrack(n)