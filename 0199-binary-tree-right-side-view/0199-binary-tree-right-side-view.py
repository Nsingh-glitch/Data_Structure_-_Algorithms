# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:return []
        q=deque()
        q.append((root,0))
        hmap=dict()
        while q:
            node,line=q.popleft()

            if line not in hmap:
                hmap[line]=node.val

            if node.right:
                q.append((node.right,line+1))
            if node.left:
                q.append((node.left,line+1))
        ans=[]
        for k in sorted(hmap.keys()):
            ans.append(hmap[k])

        return ans