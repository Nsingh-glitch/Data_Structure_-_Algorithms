class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)

        start = [-1] * 26
        end = [-1] * 26

        for i in range(n):
            ind = ord(s[i]) - ord('a')

            if start[ind] == -1:
                start[ind] = i

            end[ind] = i

        valid = [True] * 26

        for c in range(26):
            if start[c] == -1:
                continue

            j = start[c]

            while j <= end[c]:
                ind = ord(s[j]) - ord('a')

                if start[ind] < start[c]:
                    valid[c] = False
                    break

                end[c] = max(end[ind], end[c])
                j += 1

        prev = 10**9
        res = []

        for i in range(n - 1, -1, -1):
            ind = ord(s[i]) - ord('a')

            if start[ind] == i and valid[ind] and end[ind] < prev:
                res.append(s[i:end[ind] + 1])
                prev = i

        return res[::-1]