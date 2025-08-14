from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:    # find mid point
            fast = fast.next.next   # move 2
            slow = slow.next    # move 1
        
        prev = None

        while slow:     # reverse 2nd half of ll
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        left, right = head, prev

        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True
    
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        li = []

        while head:
            li.append(head.val)
            head = head.next
        
        l, r = 0, len(li) - 1

        while l <= r :
            if li[l] != li[r]:
                return False
            l += 1
            r -= 1
        
        return True