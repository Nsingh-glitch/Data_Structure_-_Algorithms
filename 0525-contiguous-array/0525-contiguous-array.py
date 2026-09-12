class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hmap=dict()
        s=0
        ans=0
        for i in range(len(nums)):
            if nums[i]==0:
                s-=1
            else:
                s+=1

            if s==0:
                ans=max(ans,i+1)
            else:
                if s not in hmap:
                    hmap[s]=i
                else:
                    ans=max(ans,i-hmap[s])

        return ans
                    

        
        