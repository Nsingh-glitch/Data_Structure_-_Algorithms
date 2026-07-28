class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m=len(p)
        n=len(s)

        def x(i,j):
            if j==m:
                if i==n:
                    return True

                return False

            first_match=i<n and (s[i]==p[j] or p[j]=='.') 

            if j+1<m and (p[j+1]=='*'):
                n_take=x(i,j+2)

                take=first_match and x(i+1,j)
                return take or n_take
            
            else:
                return first_match and  x(i+1,j+1)


        dp=[[False for _ in range(m+1)]for _ in range(n+1)]
        dp[n][m]=True
        
        for j in range(m - 2, -1, -1):
            if p[j + 1] == '*':
                dp[n][j] = dp[n][j + 2]

        for i in range(n-1,-1,-1):

            for j in range(m-1,-1,-1):
                first_match=i<n and (s[i]==p[j] or p[j]=='.') 

                if j+1<m and (p[j+1]=='*'):
                    n_take=dp[i][j+2]

                    take=first_match and dp[i+1][j]
                    dp[i][j]= take or n_take
                
                else:
                    dp[i][j]= first_match and  dp[i+1][j+1]

        return dp[0][0]




            