from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        cur = head

        while cur:
            while stack and stack[-1] < cur.val:
                stack.pop()
            stack.append(cur.val)
            cur = cur.next
        
        head = ListNode()
        cur = head
        for n in stack:
            cur.next = ListNode(n)
            cur = cur.next
        
        return head.next
    
 
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Reverse a linked list
        def reverse(head):
            prev, cur = None, head
            while cur:
                tmp = cur.next     # Save the next node
                cur.next = prev    # Reverse the link
                prev, cur = cur, tmp  # Move prev and cur forward
            return prev  # New head of reversed list

        # Step 1: Reverse the list to process from the end
        head = reverse(head)

        # Step 2: Traverse the reversed list, keeping track of the maximum seen so far
        cur = head
        cur_max = head.val  # The first node's value is the max initially

        # Step 3: Remove any node whose value is less than the maximum to its left
        while cur and cur.next:
            if cur.next.val < cur_max:
                # Skip the next node because it's smaller than the max so far
                cur.next = cur.next.next
            else:
                # Update max and move forward
                cur_max = cur.next.val
                cur = cur.next

        # Step 4: Reverse the list again to restore original order (with unwanted nodes removed)
        return reverse(head)
