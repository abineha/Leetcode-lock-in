from typing import Optional

class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            prev = None
            cur = head

            while cur:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            
            return prev
        
        l1 = reverse(l1)
        l2 = reverse(l2)

        dummy = ListNode()
        cur = dummy 
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + carry
            carry = total // 10

            cur.next = ListNode(total % 10)
            cur = cur.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return reverse(dummy.next)
