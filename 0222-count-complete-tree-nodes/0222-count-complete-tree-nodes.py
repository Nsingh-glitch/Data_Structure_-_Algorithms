# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def left_h(node):
            cnt=0
            while node:
                cnt+=1
                node=node.left

            return cnt

        def right_h(node):
            cnt=0
            while node:
                cnt+=1
                node=node.right
            return cnt

        def x(root):
            if not root:
                return 0

          
            l=left_h(root.left)
            r=right_h(root.right)
            if l==r:
                return (2**(1+l))-1
            return 1+x(root.left)+x(root.right)

        return x(root)

        