class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n=len(nums)
        return sum(nums)-n*min(nums)