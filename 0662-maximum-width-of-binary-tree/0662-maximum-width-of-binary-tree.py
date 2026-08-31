# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:return 0

        q=deque()
        q.append((root,0))
        ans=-1e9

        while q:

            l=len(q)
            x,mini=q[0]
            first=last=0

            for j in range(l):
                node,i=q.popleft()
                if j==0:first=i
                if j==l-1:last=i
                i-=mini
               
                if node.left:
                    q.append((node.left,2*i+1))
                if node.right:
                    q.append((node.right,2*i+2))
            ans=max(ans,last-first+1)
        return ans
            
            
        