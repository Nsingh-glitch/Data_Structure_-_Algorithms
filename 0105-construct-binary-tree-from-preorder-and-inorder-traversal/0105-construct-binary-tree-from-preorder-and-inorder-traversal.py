# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n=len(preorder)
        hmap=dict()
        for i in range(n):
            hmap[inorder[i]]=i
        
        

        def x(in_start,in_end,pre_start,pre_end):
            if pre_start>pre_end or in_start>in_end:
                return None

            root=TreeNode(preorder[pre_start])

            inroot=hmap[preorder[pre_start]]
            nums_left=inroot-in_start

            root.left=x(in_start,inroot-1,pre_start+1,pre_start+nums_left)
            root.right=x(inroot+1,in_end,pre_start+nums_left+1,pre_end)

            return root

        return x(0,n-1,0,n-1)
        

            


        