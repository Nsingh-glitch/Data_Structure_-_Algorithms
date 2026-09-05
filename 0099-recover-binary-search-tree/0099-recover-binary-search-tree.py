# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        st=[]
        curr=root
        prev=None
        first=second=None

        while curr or st:
            while curr :
                st.append(curr)
                curr=curr.left

            curr=st.pop()
 
            if prev and  prev.val>curr.val:
                if not first:
                    first=prev
                second=curr

            prev=curr
            curr=curr.right

        first.val,second.val=second.val,first.val
        return root