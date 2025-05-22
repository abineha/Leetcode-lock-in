from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next    # 0, 1
        while fast and fast.next:   # fast not None and hasnt reached end 
            slow = slow.next    # s+=1
            fast = fast.next.next  # f+=2

        second = slow.next # 2nd half
        slow.next = None
        prev = None

        # reverse 2nd half
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # merge 2 halves
        first, second = head, prev
        while second:
            t1, t2 = first.next, second.next # saev links
            first.next = second 
            second.next = t1
            first, second = t1, t2
        