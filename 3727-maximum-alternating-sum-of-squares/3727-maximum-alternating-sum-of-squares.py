class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort(key=lambda x: x * x)
        s1=0
        s2=0
        for i in range(n):
            if i<n//2:
                s1+=nums[i]*nums[i]
            else:
                s2+=nums[i]*nums[i]

        return s2-s1

        