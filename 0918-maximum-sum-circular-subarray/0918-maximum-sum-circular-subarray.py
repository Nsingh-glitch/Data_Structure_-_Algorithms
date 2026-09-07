class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxi=nums[0]
        mini=nums[0]
        curr_max=0
        curr_min=0
        total=0
        for a in nums:
            curr_max=max(curr_max+a,a)
            maxi=max(maxi,curr_max)
            curr_min=min(curr_min+a,a)
            mini=min(mini,curr_min)
            total+=a
        
        print(maxi,mini)
        return max(maxi,total-mini) if maxi>0 else maxi