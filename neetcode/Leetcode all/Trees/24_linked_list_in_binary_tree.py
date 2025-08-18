from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def issub(self, list_node, tree_node):
        if not list_node:
            return True
        if not tree_node or list_node.val != tree_node.val:
            return False
        
        return (self.issub(list_node.next, tree_node.left) or self.issub(list_node.next, tree_node.right))

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if self.issub(head, root):
            return  True
        if not root:
            return False
        
        return (self.isSubPath(head, root.left) or self.isSubPath(head, root.right))