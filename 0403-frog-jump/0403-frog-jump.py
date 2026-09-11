class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        dp = [set() for _ in range(n)]

        dp[0].add(0)

        for i in range(n):
            for prev in dp[i]:
                for k in range(max(1, prev - 1), prev + 2):
                    nxt = stones[i] + k

                    if nxt in stones:
                        j = stones.index(nxt)
                        dp[j].add(k)

        return len(dp[-1]) > 0