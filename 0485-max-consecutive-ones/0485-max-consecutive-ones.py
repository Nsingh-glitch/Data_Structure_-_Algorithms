class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l=0
        ans=0
        for r in range(len(nums)):
            if nums[r]==0:
                ans=max(ans,r-l)
                l=r+1
        print(r,l)
        return max(ans,r-l+1)
        