class Solution:
    def twoSum(self, nums: list[int], k: int) -> list[int]:
        hmap=dict()
        n=len(nums)
        for i in range(n):
            tmp=k-nums[i]
            if tmp in hmap:
                return [hmap[tmp],i]

            hmap[nums[i]]=i

        return -1

        