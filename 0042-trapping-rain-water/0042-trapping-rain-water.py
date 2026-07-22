class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        ans=0
        
        prfx=[0]*n
        sufx=[0]*n
        prfx[0]=height[0]
        sufx[-1]=height[-1]

        for i in range(1,n):
            prfx[i]=max(prfx[i-1],height[i])
        
        for i in range(n-2,-1,-1):
            sufx[i]=max(sufx[i+1],height[i])


        for i in range(n):
            ans+=min(prfx[i],sufx[i])-height[i]
        return ans
    

        
