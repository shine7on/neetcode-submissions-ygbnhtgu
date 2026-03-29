# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        cur = root


        while cur or stack:
            print("enter")
            while cur:
                stack.append(cur)
                # keep going to left
                cur = cur.left
                
            cur = stack.pop()
            n += 1

            print(cur.val)

            if n == k:
                return cur.val
            # go right subtree
            cur = cur.right