class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        dp=[0]*(n+1)
        curr=0
        prev=0
        for i in range(n-1,-1,-1):
            temp=curr
            curr = max(nums[i] +prev,curr)
            prev=temp

        return curr

