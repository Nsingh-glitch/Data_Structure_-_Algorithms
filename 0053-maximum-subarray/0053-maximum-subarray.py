class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max=0
        maxi=nums[0]
        for i in nums:
            curr_max=max(curr_max+i,i)

            maxi=max(maxi,curr_max)
        print(maxi,curr_max)
        
        return maxi 