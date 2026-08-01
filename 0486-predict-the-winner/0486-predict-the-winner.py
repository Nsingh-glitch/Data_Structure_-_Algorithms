class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n=len(nums )
        dp=[[0 for _ in range(n)]for _ in range(n)]

        def x(i,j):
            if i==j:
                return nums[i]

            if dp[i][j]!=-1:
                return dp[i][j]

            take_i=nums[i]-x(i+1,j)

            take_j=nums[j]-x(i,j-1)

            dp[i][j]= max(take_i,take_j)
            return dp[i][j]

        for i in range(n):
            dp[i][i]=nums[i]
        for i in range(n-2,-1,-1):
            for j in range(i+1,n):
                take_i=nums[i]-dp[i+1][j]

                take_j=nums[j]-dp[i][j-1]

                dp[i][j]=max(take_i,take_j)
        return dp[0][n-1]>=0

        