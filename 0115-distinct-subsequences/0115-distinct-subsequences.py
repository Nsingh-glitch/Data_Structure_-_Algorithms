class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m=len(s)
        n=len(t)
        dp=[[0 for _ in range(n+1)]for _ in range(m+1)]
        def x(i,j):
            if j==n:return 1
            if i==m:
                return 0

            ans=0
            if s[i]==t[j]:
                ans+=x(i+1,j+1)
           

            ans+=x(i+1,j)
            return ans

        # return x(0,0)
        dp[m][n] = 1

        for i in range(m):
            dp[i][n]=1

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                ans=0
                if s[i]==t[j]:
                    ans+=dp[i+1][j+1]

                ans+=dp[i+1][j]

                dp[i][j]=ans

        return dp[0][0]
                
                    

            