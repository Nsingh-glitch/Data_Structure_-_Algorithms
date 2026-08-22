# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # if not root:
        #     return []

        # st = [root]
        # ans = []

        # while st:
        #     node = st.pop()
        #     ans.append(node.val)   # Root
        #     if node.left:          # Left pushed second
        #         st.append(node.left)
        #     if node.right:         # Right pushed first
        #         st.append(node.right)

        # return ans[::-1]           # Reverse to get Left -> Right -> Root

    
        def x(root):
            res=[]
            if not root:
                return res
            res+=x(root.left)
            res+=x(root.right)
            res.append(root.val)
            return res
        return x(root)
