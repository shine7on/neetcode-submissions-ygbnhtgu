# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = []

        if head is None:
            return head

        # Have a pointer to the previous node (starts as None)
        # Have a pointer to the current node
        # Save the current node’s original .next (so you don’t lose the remainder)
        # Flip current.next to point to previous

        prev = None

        while head is not None:
            current = head
            next_node = current.next
            head.next = prev
            prev = head
            head = next_node
            
        return prev
        