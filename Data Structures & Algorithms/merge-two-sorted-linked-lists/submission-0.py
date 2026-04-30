# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val < list2.val:
            head = list1
            ptr = list1
            list1 = list1.next
        else:
            head = list2
            ptr = list2
            list2 = list2.next
        count = 0
        while list1 or list2:
            count += 1
            if list2 == None:
                ptr.next = list1
                return head
            if list1 == None:
                ptr.next = list2
                return head
            if list1.val < list2.val:
                ptr.next = list1
                list1 = list1.next
                ptr = ptr.next
            else:
                ptr.next = list2
                list2 = list2.next
                ptr = ptr.next
        return head
