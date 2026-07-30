class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        l=0
        r=n-1
        while l<=r:
            mid=(l+r)//2

            if mid %2==0:
                if mid+1<n and nums[mid+1]==nums[mid]:
                    l=mid+1
                else:
                    r=mid-1
            else:
                if mid-1>=0 and nums[mid-1]==nums[mid]:
                    l=mid+1
                else:
                    r=mid-1

        return nums[l]
