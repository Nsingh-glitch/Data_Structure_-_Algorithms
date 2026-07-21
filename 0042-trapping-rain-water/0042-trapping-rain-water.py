class Solution:
    def trap(self, arr: List[int]) -> int:
        n=len(arr)
        l=0
        r=n-1
        left_max=-1
        right_max=-1
        ans=0
        while r>l:
            if arr[l]<arr[r]:
                if arr[l]<left_max:
                    ans+=left_max-arr[l]
                    
                else:
                    left_max=max(left_max,arr[l])
                
                l+=1
            else:
                if arr[r]<right_max:
                    ans+=right_max-arr[r]
                    
                else:
                    right_max=max(right_max,arr[r])
                r-=1
        return ans

        