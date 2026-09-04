# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root=TreeNode(preorder[0])
        def insert(node,item):
            if node.val<item:
                if node.right==None:
                    node.right=TreeNode(item)
                else:
                    insert(node.right,item)
            if node.val>item:
                if node.left==None:
                    node.left=TreeNode(item)
                else:
                    insert(node.left,item)

        for i in range(1,len(preorder)):
            insert(root,preorder[i])

        return root