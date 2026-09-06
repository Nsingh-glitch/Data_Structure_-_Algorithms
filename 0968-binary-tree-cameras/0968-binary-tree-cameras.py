# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0



        covered=set()
        covered.add(None)
        ans=0

        def x(root,parent):
            nonlocal ans
            if root:
                x(root.left,root)
                x(root.right,root)
                if root.left not in covered or root.right not in covered:
                    covered.add(root)
                    covered.add(parent)
                    covered.add(root.left)
                    covered.add(root.right)
                    ans+=1

        x(root,None)
        if root not in covered:
            ans+=1
        return ans



            

        