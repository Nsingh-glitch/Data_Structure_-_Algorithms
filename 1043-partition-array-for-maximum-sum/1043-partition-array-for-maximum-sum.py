class Solution:
    def maxSumAfterPartitioning(self, nums: List[int], k: int) -> int:
        n=len(nums)
        dp=[-1 for _ in range(n)]
        def x(i):
            if i==n:
                return 0
            max_ele=0
            ans=0
            if dp[i]!=-1:
                return dp[i]
            for ind in range(i,min(n,i+k)):
                max_ele=max(max_ele,nums[ind])
                val=max_ele*(ind-i+1)
                ans=max(ans,val+x(ind+1))
            
            dp[i]=ans
            return ans
        return x(0)