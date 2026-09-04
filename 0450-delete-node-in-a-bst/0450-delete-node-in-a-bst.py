# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:


        def func(root):
            # find rightmost node
            while root.right:
                root = root.right
            return root

        def helper(root):
            # only right child
            if not root.left:
                return root.right

            # only left child
            elif not root.right:
                return root.left

            # both children
            last_right_child = func(root.left)
            last_right_child.right = root.right

            return root.left

        if not root:
            return None

        # deleting root
        if root.val == key:
            return helper(root)

        tmp = root

        while root:
            if root.val > key:

                # key is left child
                if root.left and root.left.val == key:
                    root.left = helper(root.left)
                    break

                root = root.left

            else:

                # key is right child
                if root.right and root.right.val == key:
                    root.right = helper(root.right)
                    break

                root = root.right

        return tmp



        