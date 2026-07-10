class Solution:
    def merge(self, arr, l, mid, h):
        cnt = 0

        # Count reverse pairs
        right = mid + 1

        for left in range(l, mid + 1):
            while right <= h and arr[left] > 2 * arr[right]:
                right += 1
            cnt += right - (mid + 1)

        # Normal merge
        temp = []
        left = l
        right = mid + 1

        while left <= mid and right <= h:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1

        while left <= mid:
            temp.append(arr[left])
            left += 1

        while right <= h:
            temp.append(arr[right])
            right += 1

        for i in range(l, h + 1):
            arr[i] = temp[i - l]

        return cnt
        
    def mergesort(self,arr,low,high):
        ans=0
        if low<high: 
            mid=(low+high)//2
            ans+= self.mergesort(arr,low,mid)
            ans+=self.mergesort(arr,mid+1,high)
            ans+=self.merge(arr,low,mid,high)
        return ans
        
    def reversePairs(self, nums: List[int]) -> int:
        return self.mergesort(nums,0,len(nums)-1)