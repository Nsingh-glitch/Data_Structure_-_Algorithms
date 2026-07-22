class Solution:
    def trap(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        lmax=rmax=0

        left=0
        right=n-1
        total=0

        while left<right:
            if nums[left]<=nums[right]:
                if nums[left]<lmax:
                    total+=lmax-nums[left]
                else:
                    lmax=nums[left]
                left+=1
            
            else:
                if nums[right]<rmax:
                    total+=rmax-nums[right]

                else:
                    rmax=nums[right]

                right-=1
        return total

        
