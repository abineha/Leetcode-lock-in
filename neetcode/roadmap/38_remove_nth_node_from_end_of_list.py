# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        o_node = ListNode(0, head)
        L, R = o_node, head 
        
        # r = head + n
        while n > 0 and R!= None:
            R = R.next
            n -= 1
        
        # move L and R till R reaches end null
        while R:
            L = L.next
            R = R.next

        # update Link
        L.next = L.next.next
        return o_node.next