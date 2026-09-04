# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def x(root, cnt):
            if not root:
                return None

            ans = x(root.left, cnt)
            if ans is not None:
                return ans

            cnt[0] += 1
            if cnt[0] == k:
                return root.val

            return x(root.right, cnt)

        return x(root, [0])
            