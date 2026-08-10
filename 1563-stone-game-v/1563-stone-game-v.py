class Solution:
    def stoneGameV(self, sV: List[int]) -> int:
        n=len(sV)
        prefix_sum=[0]*n
        prefix_sum[0]=sV[0]
        for i in range(1,n):
            prefix_sum[i]=prefix_sum[i-1]+sV[i]
        

        dp=[[-1 for _ in range(n)]for _ in range(n)]
        def x(l,r):
            if l==r:
                return 0
          
            ans=0
            if dp[l][r]!=-1:
                return dp[l][r]

            for ind in range(l,r):
                p1_val=prefix_sum[l-1]  if l-1>=0 else 0
                p1=prefix_sum[ind]-p1_val
                p2=prefix_sum[r]-prefix_sum[ind]

                # p1=sum(sV[l:ind+1])
                # p2=sum(sV[ind+1:r+1])

                if p1<p2:
                    ans=max(ans,p1 + x(l,ind))
                elif p1>p2:
                    ans=max(ans,p2 + x(ind+1,r))
                else:

                    ans=max(ans,p1+x(ind+1,r), p2+x(l,ind))

            dp[l][r]=ans
            return ans

        return x(0,n-1)


                