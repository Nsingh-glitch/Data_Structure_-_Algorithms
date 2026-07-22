class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp=1
        for i in range(1,len(nums)):
            if nums[i]>nums[temp-1]:
                nums[i],nums[temp]=nums[temp],nums[i]
                temp+=1
        return temp
