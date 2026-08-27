# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def h(node):
            if not node:
                return 0

            l=1+h(node.left)
            r=1+h(node.right)

            return max(l,r)
        def x(node):
            if not node:return True

            lh=h(node.left)
            rh=h(node.right)
            
            if abs(lh-rh)>1: return False

            if not x(node.left )or not x(node.right):
                return False

            return True

        return x(root)

        