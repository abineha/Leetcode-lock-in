from typing import Optional
from collections import deque

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def count(nums):
            swap = 0
            map = {n:i for i, n in enumerate(nums)}
            sort_nums = sorted(nums)

            for i in range(len(nums)):
                if nums[i] != sort_nums[i]:
                    ele_idx = map[sort_nums[i]]
                    nums[i], nums[ele_idx] = nums[ele_idx], nums[i]
                    map[nums[i]] = i
                    map[nums[ele_idx]] = ele_idx
                    swap += 1

            return swap
        
        q = deque([root])
        result = 0

        while q:
            lvl = []

            for i in range(len(q)):
                node = q.popleft()
                lvl.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            result += count(lvl)
        
        return result