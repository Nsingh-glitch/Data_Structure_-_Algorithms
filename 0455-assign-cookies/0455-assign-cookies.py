class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        j = 0
        cnt = 0

        for i in range(len(g)):
            while j < len(s) and s[j] < g[i]:
                j += 1

            if j == len(s):
                break

            cnt += 1
            j += 1

        return cnt