# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        hmap=dict()
        def find(root,hmap):
            if not root:
                return 0

            l=find(root.left,hmap)
            r=find(root.right,hmap)
            hmap[root]=1+l+r
            return 1+l+r
        find(root,hmap)
      

        ans=0
        def x(node):
            nonlocal ans
            if not node:return 0
            l=x(node.left)
            r=x(node.right)
            s=l+r+node.val

            if s//hmap[node]==node.val:
                ans+=1

            return s
        x(root)
        return ans
        



        