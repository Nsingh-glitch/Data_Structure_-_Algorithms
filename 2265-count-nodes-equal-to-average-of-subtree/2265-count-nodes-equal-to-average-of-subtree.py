# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:

        ans=0
        def x(node):
            nonlocal ans
            if not node:return (0,0)
            (l,l_cnt)=x(node.left)
            (r,r_cnt)=x(node.right)
            s=l+r+node.val

            n=l_cnt+r_cnt+1
            if s//n==node.val:
                ans+=1

            return (s,n)
        x(root)
        return ans
        



        