class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        st = []

        def x(node):
            if not node:
                return

            st.append(str(node.val))

            # Leaf node
            if not node.left and not node.right:
                ans.append("->".join(st))
            else:
                x(node.left)
                x(node.right)

            st.pop()

        x(root)
        return ans