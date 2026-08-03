class Solution:
    def stoneGameIII(self, sV: List[int]) -> str:
        n=len(sV)
        dp=[-1]*(n+1)

        def x(i):
            if i>=n:
                return 0

            res=-1e9
            if dp[i]!=-1:return dp[i]
            res=max(res, sV[i]-x(i+1))
            if i+1<n:
                res=max(res, sV[i] +sV[i+1]-x(i+2)) 
            if i+2<n:
                res=max(res, sV[i]+sV[i+1]+sV[i+2]-x(i+3))

            dp[i]=res
            return res
            
        t=x(0)
        if t==0:
            return "Tie"
        elif t<0:
            return "Bob"
        else:
            return "Alice"

        

        
            
        