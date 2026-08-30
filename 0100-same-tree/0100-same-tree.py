# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def x(l,r):
            if not l and not r:return True

            if not l or not r:
                return False

            return l.val==r.val and x(l.left,r.left) and x(l.right,r.right)


        return x(p,q)


