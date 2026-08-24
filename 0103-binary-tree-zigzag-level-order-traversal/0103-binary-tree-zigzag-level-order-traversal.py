# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root :
            return []


        st=[root]
        res=[]
        lr=True
        while st:
            lvl=[0]*len(st)
            n=len(st)   
            for i in range(len(st)):
                
                node=st.pop(0)

                ind=i if lr else (n-1-i)
                lvl[ind]=(node.val)

                if node.left:st.append(node.left)
                if node.right:st.append(node.right)

                
            lr=not lr
            res.append(lvl)  
        return res
           
                 
  
        return res

                
        