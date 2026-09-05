# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        vis=set()
        st=[]
        while root or st:
            while root:
                st.append(root)
                root=root.left

            root=st.pop()
            
            if k-(root.val)in vis:
                return True
            vis.add(root.val)

            root=root.right

        return False
            
        