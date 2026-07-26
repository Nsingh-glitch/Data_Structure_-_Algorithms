# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:return 0
        def x(root,maxi):
            if not root:return 0

            cnt=0
            
            if root.val>=maxi:
                cnt+=1
                maxi=root.val 
            print(maxi,cnt)               

            l=x(root.left,maxi)
            r=x(root.right,maxi)

            return cnt+l+r

        
        return x(root,root.val)


        