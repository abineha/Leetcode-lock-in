from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Step 1: Move prev to node before left
        for _ in range(left - 1):
            prev = prev.next

        # Step 2: Reverse sublist
        cur = prev.next
        end = None
        for _ in range(right - left + 1):
            temp = cur.next
            cur.next = end
            end = cur
            cur = temp

        # Step 3: Reconnect
        prev.next.next = cur
        prev.next = end

        return dummy.next
