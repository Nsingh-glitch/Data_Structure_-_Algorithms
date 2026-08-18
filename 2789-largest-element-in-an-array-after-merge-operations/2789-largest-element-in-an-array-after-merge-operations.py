class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        n=len(nums)
        ans=-1e9
        cnt=0
      
        for i in range(n-1,-1,-1):
            if cnt>=nums[i]:
                cnt+=nums[i]
            else:
                
                cnt=nums[i]
            ans=max(ans,cnt)
         

        return ans

        