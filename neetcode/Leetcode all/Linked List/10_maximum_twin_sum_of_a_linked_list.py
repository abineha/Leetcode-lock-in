from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            # reverse it
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        result = 0
        while slow:
            result = max(result, slow.val + prev.val)   # slow -> right half | prev -> left half in rerverse
            slow = slow.next
            prev = prev.next
        
        return result