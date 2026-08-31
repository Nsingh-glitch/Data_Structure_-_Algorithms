# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def x(root,p,q):
            if not root:
                return None
            
            if root==p or root==q:return root

            l=x(root.left,p,q)
            r=x(root.right,p,q)
            if not l:
                return r
            elif not r:return l
            else:
                return root

        return x(root,p,q)
        