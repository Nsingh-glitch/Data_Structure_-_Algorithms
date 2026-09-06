# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        # 0-->Not covered
        # 1-->Covered
        # 2-->Camera Placed
        self.cam=0
        def dfs(root):
            if not root:
                return 1
            
            l=dfs(root.left)
            r=dfs(root.right)

            if l==0 or r==0:
                self.cam+=1
                return 2

            elif l==2 or r==2:
                return 1
            
            else:
                return 0

        if dfs(root) == 0:
            self.cam += 1

        return self.cam

        