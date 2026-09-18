class Solution:
    def minPathSum(self, mat: list[list[int]]) -> int:
        m=len(mat)
        n=len(mat[0])
    
        dp=[[0 for _ in range(n)]for _ in range(m)]

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):

                if  i==m-1 and j==n-1:
                    dp[i][j]=mat[i][j]
                else:
                    l=dp[i+1][j] if i+1 <m else 1e9
                    r=dp[i][j+1] if j+1<n else 1e9

                    dp[i][j]=mat[i][j]+min(l,r)
        return dp[0][0]
        