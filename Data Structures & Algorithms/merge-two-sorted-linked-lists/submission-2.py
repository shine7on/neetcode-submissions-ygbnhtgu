# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        head = dummy

        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                temp = list1.next
                dummy.next = list1
                dummy = dummy.next
                list1 = temp
            else:
                temp = list2.next
                dummy.next = list2
                dummy = dummy.next
                list2 = temp
        
        if list1:
            dummy.next = list1
        elif list2:
            dummy.next = list2
        
        return head.next