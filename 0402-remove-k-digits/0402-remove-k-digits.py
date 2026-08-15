class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)

        if n <= k:
            return "0"

        st = []

        for i in num:
            while st and k and st[-1] > i:
                st.pop()
                k -= 1

            st.append(i)

        # If k is still remaining, remove from end
        while st and k:
            st.pop()
            k -= 1

        # Remove leading zeroes
        while st and st[0] == '0':
            st.pop(0)

        return ''.join(st) if st else "0"