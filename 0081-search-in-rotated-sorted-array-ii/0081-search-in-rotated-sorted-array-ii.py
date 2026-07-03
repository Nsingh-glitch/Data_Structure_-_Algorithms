class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)     
        low=0
        high=n-1
        
        while low<=high:
            mid=(low+high)//2

            if nums[mid]==target:
                return True

            if nums[low]==nums[high]==nums[mid]:
                low+=1
                high-=1
                continue

            elif nums[mid]>=nums[low]:
                if nums[low]<=target and nums[mid]>=target:
                    high=mid-1
                else:
                    low=mid+1
            else:
                if nums[high]>=target and nums[mid]<=target:
                    low=mid+1
                else:
                    high=mid-1
        return False
