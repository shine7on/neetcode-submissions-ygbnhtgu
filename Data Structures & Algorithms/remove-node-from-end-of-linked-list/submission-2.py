# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # reverse
        prev, curr = None, head

        while curr != None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # reversed list
        rev_li = prev
        
        # how to get the nth from start
        prev2 = []

        if n == 1:
            if rev_li.next is None:
                return rev_li.next
            else: rev_li = rev_li.next
        else:
            while n > 1 and prev.next is not None:
                prev2 = prev # one before delete one
                prev = prev.next # the one you delete
                n -= 1
            
            prev2.next = prev.next
        
        # reverse
        prev3, curr2 = None, rev_li

        if curr2 is None:
            return 

        while curr2 != None:
            next_node = curr2.next
            curr2.next = prev3
            prev3 = curr2
            curr2 = next_node
        
        return prev3


        
        

        