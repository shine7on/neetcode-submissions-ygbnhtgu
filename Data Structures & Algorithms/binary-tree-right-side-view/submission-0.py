# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        deque = collections.deque([root])
        res = []

        while deque:
            rightSide = None
            qlen = len(deque)

            for i in range(qlen):
                node = deque.popleft()
                if node:
                    rightSide = node
                    deque.append(node.left) # left is first
                    deque.append(node.right)
            
            if rightSide:
                res.append(rightSide.val)
        
        return res
