# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if root == q or root == p:
            return root
        
        # if p is in right and q is in leff -> return root
        left = self.findVal(root.left, p.val) and self.findVal(root.left, q.val)
        right = self.findVal(root.right, p.val) and self.findVal(root.right, q.val)

        print(left, right)

        if left:
            return self.lowestCommonAncestor(root.left, p, q)
        elif right:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

    
    def findVal(self, root, val):
        if root == None:
            return False   
        if root.val == val:
            return True
        
        return self.findVal(root.right, val) or self.findVal(root.left, val)