from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0 # current visited node count
        stack = [] # iterative soln
        curr = root # start from root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left # keep going left take  all into count till lowest num -> none

            curr = stack.pop() # reached lowest num
            n += 1
            if n == k:
                return curr.val
            
            # all of roots left side calculated but didnt reaach k so go right
            curr = curr.right
    