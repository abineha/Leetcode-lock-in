from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == None or len(lists) == 0:
            return None 
        
        while len(lists) > 1:   # merge LL till we get 1 sorted 1 LL
            merged_lists = []

            for i in range(0, len(lists), 2):    # take 2 LL and merge and add to total merged_lists
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                merged_lists.append(self.merge_2_lists(l1,l2))
            lists = merged_lists
        
        return lists[0]
    
    def merge_2_lists(self, l1, l2):
        o_node = ListNode()
        head = o_node
    
        while l1 and l2:
            if l1.val < l2.val:
                o_node.next = l1
                l1 = l1.next
            else:
                o_node.next = l2
                l2 = l2.next
                
            o_node = o_node.next

        o_node.next = l1 or l2
        return head.next