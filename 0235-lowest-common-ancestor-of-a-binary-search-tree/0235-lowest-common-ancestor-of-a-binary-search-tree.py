# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, node: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr=node
        while curr:
            if curr.val>p.val and curr.val>q.val:
                curr=curr.left

            elif curr.val<p.val and curr.val<q.val:
                curr=curr.right

            else:
                return curr

