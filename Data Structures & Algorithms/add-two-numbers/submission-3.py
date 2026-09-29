# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        array1, array2 = "", ""

        while l1:
            array1 += str(l1.val)
            l1 = l1.next
        
        while l2:
            array2 += str(l2.val)
            l2 = l2.next
        
        res = int(array1[::-1]) + int(array2[::-1])
        dummy = ListNode(0)
        head = dummy

        for char in str(res)[::-1]:
            head.next = ListNode(char)
            head = head.next
    
        return dummy.next