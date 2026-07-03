class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]

        low, high = 0, len(nums) - 1

        while low < high:
            mid = (low + high) // 2

            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        return nums[low]