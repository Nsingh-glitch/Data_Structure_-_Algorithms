class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n=len(stones)
        prefix=[0]*n
        prefix[0]=stones[0]
        dp=[0]*(n+1)
        for i in range(1,n):
            prefix[i]=prefix[i-1]+stones[i]
        

        def solve(i):
            if i==n-1:
                return prefix[n-1]
            if dp[i]!=-1:return dp[i]

            take=prefix[i]-solve(i+1)

            n_take=solve(i+1)

            dp[i]= max(take,n_take)
            return dp[i]

   


        dp[n-1]=prefix[n-1]
        for i in range(n-2,0,-1):
            take=prefix[i]-dp[i+1]

            n_take=dp[i+1]

            dp[i]=max(take,n_take)

        return dp[1]
        