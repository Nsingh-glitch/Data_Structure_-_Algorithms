class Solution:
    def jump(self, nums: List[int]) -> int:
        ans=0
        l=r=0
        jumps=0
        n=len(nums)

        while r<n-1:
            jumps+=1
            
            maxi=0
            for ind in range(l,r+1):
                maxi=max(maxi,ind+nums[ind])
            l=r+1
            r=maxi

        return jumps