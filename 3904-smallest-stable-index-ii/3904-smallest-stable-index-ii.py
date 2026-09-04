class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)

        maxi=[0]*n
        maxi[0]=nums[0]
        mini=[0]*n
        mini[-1]=nums[-1]
        
        for i in range(1,n):
            maxi[i]=max(maxi[i-1],nums[i])
            
        for i in range(n-2,-1,-1):
            mini[i]=min(mini[i+1],nums[i])


        ans=-1
        for i in range(n):
            if maxi[i]-mini[i]<=k:
                tmp= maxi[i]-mini[i]
                print(tmp)
                ans=i
                break

        return ans