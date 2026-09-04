# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, node: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def x(root):
            if not root:
                return root

            if root.val>p.val and root.val >q.val:
                return x(root.left)

            if root.val<p.val and root.val<q.val:
                return x(root.right)

            return root

        return x(node)
        