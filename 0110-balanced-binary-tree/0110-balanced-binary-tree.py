# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:return True
        def h(node):
            if not node:
                return 0

            l=h(node.left)
            if l==-1:return -1
            r=h(node.right)
            if r==-1:return -1
            if abs(l-r)>1:return -1

            return 1+max(l,r)


        return h(root)>0

        