# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi = [-1e9]

        def x(node):
            if not node:
                return 0

            left = max(0,x(node.left))


            right = max(0,x(node.right))
           

            maxi[0] = max(maxi[0],node.val+left + right) 
            return node.val + max(left, right) 
        x(root)
        return maxi[0]