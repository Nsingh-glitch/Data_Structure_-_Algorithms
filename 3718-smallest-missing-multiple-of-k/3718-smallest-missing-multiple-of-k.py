class Solution:
    def missingMultiple(self, nums: list[int], k: int) -> int:
        nums.sort()
        x = k
        for i in nums:
            if i == x:
                x += k
        return x
