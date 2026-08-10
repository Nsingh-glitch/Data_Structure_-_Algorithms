class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp=[-1 ]*100001
        def x(n):
            if n<=0:
                return False
            if dp[n]!=-1:
                return dp[n]
            i=1
            while i*i<=n:
                if not x(n-i*i):
                    dp[n]=True
                    return True

                i+=1
            dp[n]=False
            return False

        return x(n)
        