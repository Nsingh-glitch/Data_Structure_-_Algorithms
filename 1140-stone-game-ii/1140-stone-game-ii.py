class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n=len(piles)
        dp=[[[-1 for _ in range(n+1)]for _ in range(n)]for _ in range(2)]
        def func(p,i,M):
            if i>=n:
                return 0

            stones=0
            if dp[p][i][M]!=-1:
                return dp[p][i][M]

            res=-1 if p==1 else 1e9 


            for x in range(1,min(2*M,n-i)+1):
                stones+=piles[i+x-1]

                if p==1:
                    res=max(res,stones+func(0 ,i+x ,max(M,x)))

                else:
                    res=min(res,func(1 ,i+x ,max(M,x)) )

            dp[p][i][M]=res
            return res

        return func(1,0,1)
        