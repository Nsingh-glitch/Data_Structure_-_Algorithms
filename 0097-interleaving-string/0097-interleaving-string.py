class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        N = m + n

        if len(s3) != N:
            return False

        dp = [[False] * (n + 1) for _ in range(m + 1)]

        dp[m][n] = True
        for i in range(m - 1, -1, -1):
            k = i + n
            dp[i][n] = s1[i] == s3[k] and dp[i + 1][n]

        for j in range(n - 1, -1, -1):
            k = m + j
            dp[m][j] = s2[j] == s3[k] and dp[m][j + 1]


        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                k = i + j

                dp[i][j] = (
                    (s1[i] == s3[k] and dp[i + 1][j]) or
                    (s2[j] == s3[k] and dp[i][j + 1])
                )

        return dp[0][0]