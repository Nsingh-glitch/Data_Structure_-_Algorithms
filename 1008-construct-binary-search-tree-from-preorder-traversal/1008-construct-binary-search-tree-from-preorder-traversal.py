# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        ub=sys.maxsize
        n=len(preorder)
        i=[0]
        def x(i,ub):
            if i[-1]==n or ub<preorder[i[-1]]:
                return None

            new=TreeNode(preorder[i[-1]])
            i[0]+=1
            new.left=x(i,new.val)
            new.right=x(i,ub)
            return new

        return x(i,ub)
        