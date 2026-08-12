class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        hmap = {}
        l = 0
        ans = 0

        for r in range(len(nums)):
            hmap[nums[r]] = hmap.get(nums[r], 0) + 1

            while hmap[nums[r]] > k:
                hmap[nums[l]] -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans