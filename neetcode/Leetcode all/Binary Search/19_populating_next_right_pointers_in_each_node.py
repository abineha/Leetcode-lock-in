from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        cur, next = root, root.left if root else None

        while cur and next:
            cur.left.next = cur.right   # reach next layer and start assigning 'next'
            
            if cur.next:    # cur layer has more nodes
                cur.right.next = cur.next.left   # reach next layer and start assigning 'next'
            
            cur = cur.next  # move right of cur layer

            if not cur: # move cur and next to next layer each
                cur = next
                next = cur.left
        
        return root