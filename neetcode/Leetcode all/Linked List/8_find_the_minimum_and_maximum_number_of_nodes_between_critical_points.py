from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> list[int]:
        def critical(prev, cur, next):
            return ((prev.val > cur.val and cur.val < next.val) or(prev.val < cur.val and cur.val > next.val))
        
        prev, cur = head, head.next
        next = cur.next
        min_d, max_d = float("inf"), float("-inf")
        prev_crit_idx, first_crit_idx = 0, 0
        i = 1   # index of cur node

        while next:
            if critical(prev, cur, next):
                if first_crit_idx:
                    max_d = i - first_crit_idx
                    min_d = min(min_d, i-prev_crit_idx)
                else:
                    first_crit_idx = i
                
                prev_crit_idx = i
            
            prev, cur = cur, next
            next = cur.next
            i += 1
        
        if min_d == float('inf'):
            min_d = max_d = -1

        return [min_d, max_d]