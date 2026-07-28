class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        ans = [0] * (m + n)

        # Multiply from right to left
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                d1 = ord(num1[i]) - ord('0')
                d2 = ord(num2[j]) - ord('0')

                product = d1 * d2

                p1 = i + j
                p2 = i + j + 1

                total = ans[p2] + product

                ans[p2] = total % 10
                ans[p1] += total // 10

        # Remove leading zeros
        i = 0
        while i < len(ans) - 1 and ans[i] == 0:
            i += 1

        return ''.join(str(d) for d in ans[i:])