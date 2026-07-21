class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n=len(nums)
        ans=[] 
        for i in range(n-2):
            l=i+1
            r=n-1
            if  i>0 and nums[i]==nums[i-1]:

                continue
                
            while l<r:
                s=nums[l]+nums[r]

                if s == -nums[i]:
                    ans.append([nums[i], nums[l], nums[r]])

                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    while l < r and nums[r] == nums[r + 1]:
                        r-=1
                elif -nums[i]>s:
                    l+=1
                else:
                    r-=1
        return ans