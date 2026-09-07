class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        n = len(s)
        prev = [0] * (n + 1)
        last_seen = [0] * 26

        for i in range(1, n + 1):
            idx = ord(s[i - 1]) - ord('a')
            prev[i] = last_seen[idx]
            last_seen[idx] = i

        dp = [0] * (n + 1)

        def solve(i):
            if i == 0:
                return 1

            if dp[i] != -1:
                return dp[i]

            total = 2 * solve(i - 1)

            if prev[i] != 0:
                total -= solve(prev[i] - 1)

            dp[i] = total % MOD
            return dp[i]

        # return (solve(n) - 1) % MOD
        
        dp[0]=1
        for i in range(1,n+1):


            total = 2 * dp[i - 1]

            if prev[i] != 0:
                total -= dp[prev[i] - 1]

            dp[i] = total % MOD

        return (dp[n]-1)% MOD