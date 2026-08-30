class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mini=1e9
        min_ind=-1
        maxi=-1e9
        max_ind=-1

        for i in range(len(nums)):
            if nums[i]>maxi:
                maxi=nums[i]
                max_ind=i
            if nums[i]<mini:
                mini=nums[i]
                min_ind=i
        ans=1e9
        n=len(nums)

        ans=min(ans,max(min_ind,max_ind)+1)

        ans=min(ans,max(n-min_ind,n-max_ind))

        ans=min(ans,min(min_ind+1,n-min_ind)+min(max_ind+1,n-max_ind))
        return ans

            
        