class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lst_ind=0
        for i in range(1,len(nums)):
            if nums[i]>nums[lst_ind]:
                nums[i],nums[lst_ind+1]=nums[lst_ind+1],nums[i]
                lst_ind+=1
        return lst_ind+1        