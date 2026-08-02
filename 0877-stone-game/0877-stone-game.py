class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        def x(i,j):
            if i==j:
                return piles[i]

            take_i=piles[i]-x(i+1,j)

            take_j=piles[j]-x(i,j-1)

            return max(take_i,take_j)

        
        # return x(0,len(piles)-1)>=0
        n=len(piles)
        dp=[[-1 for _ in range(n)]for _ in range(n)]

        def x(l,r):
            if l>r:return 0
            if l==r:return piles[l]

            if dp[l][r]!=-1:
                return dp[l][r]

            left=piles[l]+min(x(l+1,r-1),x(l+2,r))

            right=piles[r]+min(x(l+1,r-1),x(l,r-2))

            dp[l][r]= max(left,right) 
            return dp[l][r]

        

        toat=sum(piles)       
        p1=x(0,n-1)
        p2=toat-p1

        return p1>=p2