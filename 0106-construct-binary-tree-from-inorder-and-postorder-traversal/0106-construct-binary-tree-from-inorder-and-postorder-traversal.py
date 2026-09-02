# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n=len(inorder)
        hmap=dict()
        for i in range(n):
            hmap[inorder[i]]=i

        def x(post_start,post_end,in_start,in_end):
            if post_start>post_end or in_start>in_end:
                return None

            root=TreeNode(postorder[post_end])
            ind=hmap[postorder[post_end]]
            d_l=ind-in_start
            d_r=in_end-ind

            
            root.left=x(post_start,post_start+d_l-1,in_start,ind-1)
            root.right=x(post_start+d_l,post_end-1,ind+1,in_end)

            return root

        return x(0,n-1,0,n-1)