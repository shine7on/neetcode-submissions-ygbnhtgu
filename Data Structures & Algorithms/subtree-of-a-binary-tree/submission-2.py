# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == subRoot == None:
            print("Both None")
            return True

        if root == None or subRoot == None:
            print("One None")
            return False

        if root.val == subRoot.val:
            if self.isSameTree(root, subRoot):
                return True
            
        print(f"did not happen {root.val, subRoot.val}")
        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)

    
    def isSameTree(self, root, sub):
        if root == sub == None:
            print("Both None")
            return True

        if root == None or sub == None or root.val != sub.val:
            print("wrong")
            return False

        if root.val == sub.val:
            return self.isSameTree(root.left, sub.left) and self.isSameTree(root.right, sub.right)