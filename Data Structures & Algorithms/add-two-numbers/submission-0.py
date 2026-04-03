# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        cur1,cur2 = l1, l2
        val1, val2 = 0, 0
        i = 1

        while cur1:
            val1 += cur1.val * i
            cur1 = cur1.next
            i *= 10

        i = 1
        while cur2:
            val2 += cur2.val * i
            cur2 = cur2.next
            i *= 10
        
        val1 += val2

        res = ListNode()
        head = res
        i, prev = 10, 0

        print(val1)

        while val1 > 0:
            res.val = val1 % i * 10 // i
            val1 = val1 - val1 % i
            if val1 == 0:
                return head
            print(val1, res.val, i)
            i *= 10
            res.next = ListNode()
            res = res.next

        
        return head
