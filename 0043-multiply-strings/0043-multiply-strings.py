class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        def convert(s):
            num = 0
            for ch in s:
                num = num * 10 + (ord(ch) - ord('0'))
            return num

        def int_to_string(num):
            if num == 0:
                return "0"

            chars = []
            while num > 0:
                chars.append(chr(num % 10 + ord('0')))
                num //= 10

            chars.reverse()
            return "".join(chars)

        m = len(num1)
        e2 = convert(num2)

        mult = 1
        ans = 0

        for i in range(m - 1, -1, -1):
            digit = ord(num1[i]) - ord('0')
            ans += digit * e2 * mult
            mult *= 10

        return int_to_string(ans)