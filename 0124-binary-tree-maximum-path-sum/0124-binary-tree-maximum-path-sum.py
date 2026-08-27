# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans=[-1e9]
        def x(root,ans):
            if not root:
                return 0

            lh=max(0,x(root.left,ans))
            rh=max(0,x(root.right,ans))
            ans[0]=max(ans[0] ,root.val+lh+rh)

            return root.val+max(lh,rh)
        x(root,ans)
        return ans[0]
        