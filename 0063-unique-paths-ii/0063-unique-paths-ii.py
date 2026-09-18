class Solution:
    def uniquePathsWithObstacles(self, mat: list[list[int]]) -> int:
        
        m=len(mat)
        n=len(mat[0])

        if mat[m-1][n-1]==1:
            return 0
            
        dp=[[0 for _ in range(n)]for _ in range(m)]

        dp[m-1][n-1]=1

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if mat[i][j]==1:
                    dp[i][j]=0

                elif i==m-1 and j==n-1:
                    dp[i][j]=1
                else:
                    l=dp[i+1][j] if i+1 <m else 0
                    r=dp[i][j+1] if j+1<n else 0

                    dp[i][j]=l+r
        return dp[0][0]