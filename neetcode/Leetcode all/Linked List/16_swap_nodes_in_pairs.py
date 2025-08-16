from typing import Optional

class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
        
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, cur = dummy, head

        while cur and cur.next:
            # initialise
            cur_next = cur.next
            next_pair = cur.next.next

            # reverse
            cur_next.next = cur
            cur.next = next_pair
            prev.next = cur_next

            # next set
            prev = cur
            cur = next_pair
        
        return dummy.next