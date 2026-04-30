# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hm = {}
        if not head:
            return False
        ptr = head.next
        while ptr!=None and ptr.next != None:
            ptr = ptr.next.next
            head=head.next
            if ptr == head:
                return True
        return False