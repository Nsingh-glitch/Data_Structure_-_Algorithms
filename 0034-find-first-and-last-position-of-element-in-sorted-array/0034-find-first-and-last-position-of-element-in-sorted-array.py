class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=0
        r=len(nums)-1
  
        def f1(l,h):
            ans=-1
            while l<=h:
                mid=(l+h)//2
                
                if nums[mid]==target:
                    ans=mid
                    h=mid-1
                elif nums[mid]<target:
                    l=mid+1
                else:
                    h=mid-1
            return ans

        def l1(l,h):
            ans=-1
            while l<=h:
                mid=(l+h)//2
                
                if nums[mid]==target:
                    ans=mid
                    l=mid+1
                elif nums[mid]<target:
                    l=mid+1
                else:
                    h=mid-1
            return ans
        f= f1(0,len(nums)-1)
        l=l1(0,len(nums)-1)
        return f,l
        
        