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

# we check if any child is uncovered or not

            if l==0 or r==0:
                self.cam+=1
                return 2
#then we check if childs contain camera if yes then curr node is already covered
            elif l==2 or r==2:
                return 1

#and if curr node is not covered and also not camera placed we return 0
#so in next call camera can be put there
            else:
                return 0

        if dfs(root) == 0:
            self.cam += 1

        return self.cam


"""TC : O(n) Travesing all the nodes
    SC: O(h) RSS
"""
        