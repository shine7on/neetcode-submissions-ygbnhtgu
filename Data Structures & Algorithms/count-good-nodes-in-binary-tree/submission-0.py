# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    count = 0

    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxN):
            if not node:
                return

            if node.val >= maxN:
                self.count += 1
            else:
                node.val = maxN

            right = dfs(node.right, node.val)
            left = dfs(node.left, node.val)
        
        dfs(root, -101)

        return self.count



