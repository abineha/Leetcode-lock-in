from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-101, head)
        prev, cur = dummy, head

        while cur:
            temp = cur.next
            if cur.val == prev.val:
                prev.next = temp
            else:
                prev = cur
            cur = temp
        
        return dummy.next