class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n=len(nums)
        dp=[[-1 for _ in range(n)]for _ in range(n)]

        def x(i,j):
            if i==j:
                return nums[i]

            if dp[i][j]!=-1:
                return dp[i][j]

            take_i=nums[i]-x(i+1,j)

            take_j=nums[j]-x(i,j-1)

            dp[i][j]= max(take_i,take_j)
            return dp[i][j]

        return x(0,len(nums)-1)>=0

        