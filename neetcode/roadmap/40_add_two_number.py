from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        o_node = ListNode()
        curr = o_node
        carry = 0

        while l1 or l2 or carry:
            v1, v2 = l1.val if l1 else 0, l2.val if l2 else 0
            sum = v1 + v2 + carry
            carry = sum // 10
            digit = sum % 10
            curr.next = ListNode(digit)

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        
        return o_node.next