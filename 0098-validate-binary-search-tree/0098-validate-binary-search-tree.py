# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        maxi=sys.maxsize
        mini=-sys.maxsize-1

        def x(root,l,r):
            if not root:
                return True

            if root.val <=l or root.val >=r:
                return False


            return x(root.left,l,root.val) and x(root.right,root.val,r)

        return x(root,mini,maxi)
            