class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mini=min(nums)
        maxi=max(nums)
        ans=[]
        nums=set(nums)
        for i  in range(mini,maxi+1):
            if i not in nums:
                ans.append(i)

        return ans

        