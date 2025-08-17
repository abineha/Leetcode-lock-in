from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n, cur = 0, head

        while cur:
            cur = cur.next
            n += 1

        base, remain = n // k, n % k
        cur, result = head, []

        for i in range(k):
            result.append(cur)
            
            for j in range(base -1 + (1 if remain else 0)):
                if not cur:
                    break
                
                cur = cur.next
            
            remain -= 1 if remain else 0

            if cur:
                cur.next, cur = None, cur.next

        return result