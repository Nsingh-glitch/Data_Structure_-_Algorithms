# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        curr=root
        while curr:
            if curr.left==None:
                ans.append(curr.val)
                curr=curr.right

            else:
                tmp=curr.left
                while tmp.right and tmp.right!=curr:
                    tmp=tmp.right

                if tmp.right==None:
                    ans.append(curr.val)
                    tmp.right=curr
                    curr=curr.left
                else:
                    tmp.right=None
                    
                    curr=curr.right
        return ans