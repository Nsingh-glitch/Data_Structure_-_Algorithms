class Solution:
    def rob(self, nums: list[int]) -> int:
        def x(l,r):
            curr=nums[r]
            prev=0
            for i in range(r-1,l-1,-1):
                temp=curr
                curr=max(curr,nums[i]+prev)
                prev=temp

            return curr

        n=len(nums)

        return max(x(0,n-2),x(1,n-1))
        