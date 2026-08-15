class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n=len(nums)
        tot=0
        all_zero=True

        for x in nums:
            tot^=x
            if x>0:
                all_zero=False
        if tot>0:
            return n

        return n-1 if all_zero==False else 0

