class Solution:
    def numberOfSets(self, n: int, final_k: int) -> int:
        
        mod=(10**9)+7
        dp=[[0 for _ in range(n+1)]for _ in range(final_k+1)]
        def x(k,i):
            if i>=n:
                return 0
            if k==0:
                return 1
            if dp[k][i]!=-1:
                return dp[k][i]

            skip=x(k,i+1)
            take=0
            for j in range(i+1,n):
                take+=x(k-1,j)%mod

            dp[k][i]=(take+skip)%mod
            return dp[k][i]


        for i in range(n):
            dp[0][i]=1

        for k in range(1,final_k+1):

            prev_row=[0]*(n+1)
            for y in range(n-1,-1,-1):
                prev_row[y]=prev_row[y+1]+dp[k-1][y]

            for i in range(n-1,-1,-1):
                
                skip=dp[k][i+1]%mod
                take=prev_row[i+1]%mod


                dp[k][i]=(take+skip)%mod

        return dp[final_k][0]%mod

