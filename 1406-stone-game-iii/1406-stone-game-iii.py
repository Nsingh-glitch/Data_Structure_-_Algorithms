class Solution:
    def stoneGameIII(self, sV: List[int]) -> str:
        n=len(sV)
        dp=[0]*(n+1)

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

        dp[n]=0

        for i in range(n-1,-1,-1):
            res=-1e9

            res=max(res,sV[i]-dp[i+1])
            if i+1<n:
                res=max(res,sV[i]+sV[i+1]-dp[i+2])
            if i+2<n:
                res=max(res,sV[i]+sV[i+1]+sV[i+2]-dp[i+3])
            
            dp[i]=res

            
            

        t=dp[0]
        if t==0:
            return "Tie"
        elif t<0:
            return "Bob"
        else:
            return "Alice"

        

        
            
        