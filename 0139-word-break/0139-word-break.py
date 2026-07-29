class Solution:
    def wordBreak(self, s: str, wd: List[str]) -> bool:
        wd=set(wd)
        n=len(s)

        def x(i):
            if i==n:
                return True

            for ind in range(i+1,n+1):
                if s[i:ind] in wd:
                    if x(ind):
                        return True

            return False

    
        
        dp=[False]*(n+1)
        dp[n]=True

        for i in range(n-1,-1,-1):
            for ind in range(i+1,n+1):
                if s[i:ind] in wd:
                    if dp[ind]:
                        dp[i]=True

           

        return dp[0]