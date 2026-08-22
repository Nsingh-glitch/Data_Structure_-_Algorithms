# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:return True
        
        def h(root):
            if not root:return 0
            hl=h(root.left)
            hr=h(root.right)

            if hl==-1 or hr==-1:return -1
            if abs(hl-hr)>1:return -1

            return 1+max(hl,hr)

        ans= h(root)
        if ans==-1:return False
        return True
        