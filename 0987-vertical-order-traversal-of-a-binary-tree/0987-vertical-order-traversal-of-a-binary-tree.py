# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes=[]
        queue = deque([(root, 0, 0)])  # node, row, col
        while queue:
            node, row, col = queue.popleft()
            if node:
                nodes.append((col, row, node.val))
                queue.append((node.left, row + 1, col - 1))
                queue.append((node.right, row + 1, col + 1))

        # Sort nodes first by column, then by row, then by value
        nodes.sort()

        res = []
        prev_col = float('-inf')

        for col, row, val in nodes:
            if col != prev_col:
                res.append([])
                prev_col = col
            res[-1].append(val)

        return res