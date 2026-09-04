# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        st=[]
        prev=None
        while st or root:
            while root:
                st.append(root)
                root=root.left

            root=st.pop()
            if prev!=None and root.val<=prev:return False
            prev=root.val
            root=root.right        

        return True