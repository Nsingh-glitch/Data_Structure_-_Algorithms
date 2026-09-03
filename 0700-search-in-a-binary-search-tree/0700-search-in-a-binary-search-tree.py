# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:return root
        def x(root):
            if root.val==val:
                return root

            if root.left and root.val>val:
                return x(root.left)
            if root.right and root.val<val:
                return x(root.right)

            return None

        return x(root)

            
        