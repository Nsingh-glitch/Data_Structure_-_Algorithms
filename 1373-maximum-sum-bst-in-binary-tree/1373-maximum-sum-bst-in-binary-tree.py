class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        int_max = 1e9
        int_min = -1e9
        ans=0

        def x(root):
            nonlocal ans
            if not root:
                return (0, int_max, int_min)

            s1, l_mini, l_maxi = x(root.left)
            s2, r_mini, r_maxi = x(root.right)

            if  root.val > l_maxi and r_mini > root.val:
                tmp = s1 + s2 + root.val
                ans=max(ans,tmp)
                return (tmp, min(l_mini, root.val), max(r_maxi, root.val))

            else:
                return (0, int_min, int_max)

 

        x(root)
        return ans