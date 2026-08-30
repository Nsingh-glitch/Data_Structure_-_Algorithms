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
        l, r=min(min_ind,max_ind), max(min_ind,max_ind)

        return min(r+1,n-l,l+1+n-r)

            
        