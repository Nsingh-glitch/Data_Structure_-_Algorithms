class Solution:
    def rob(self, nums: list[int]) -> int:
        def x(i):
            if i>=len(nums):
                return 0
            
            take=nums[i]+x(i+2)

            skip=x(i+1)

            return max(take,skip)

        n=len(nums)
        dp=[0]*(n+1)
        dp[n-1]=nums[-1]
        for i in range(n-2,-1,-1):
            take=nums[i]+dp[i+2]
            skip=dp[i+1]
            dp[i]=max(take,skip)
        return dp[0]