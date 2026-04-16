# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        res = []
        
        def search(node1, node2):

            if not node1:
                return res
            elif node1.val == node2.val:
                res.append(node1)

            search(node1.right, node2)
            search(node1.left, node2)

            return res

        def checkSub(node1, node2):
            if node1 and not node2 or not node1 and node2:
                return False
            elif not node1 and not node2:
                return True
            print(node1.val, node2.val)
            if node1 and node2 and node1.val == node2.val:
                return checkSub(node1.right, node2.right) and checkSub(node1.left, node2.left)
            elif node1.val != node2.val:
                return False

        rootRs = search(root, subRoot)

        print(rootRs)

        for r in rootRs:
            if checkSub(r, subRoot):
                return True
        
        return False

        