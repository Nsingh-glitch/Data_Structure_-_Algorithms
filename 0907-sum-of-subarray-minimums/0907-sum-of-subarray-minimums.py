class Solution:
    def sumSubarrayMins(self, arr):
        stack = []
        ans = 0
        n = len(arr)

        for i in range(n + 1):
            current = arr[i] if i < n else 0

            while stack and (i == n or arr[stack[-1]] >current):
                mid = stack.pop()

                if not stack:
                    left = mid + 1
                else:
                    left = mid - stack[-1]

                right = i - mid

                ans += arr[mid] * left * right

            stack.append(i)

        return ans%1000000007