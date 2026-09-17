class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n=len(arr)
        last_min=[1e9]*n
        l=0
        curr=0
        res=1e9
        best_l=1e9
        for r in range(n) :
            curr+=arr[r]
            while curr>target and l<r:
                curr-=arr[l]
                l+=1
            
            if curr==target:
                if l>0 and last_min[l-1]!=1e9:
                    res=min(res,r-l+1+last_min[l-1])


                best_l=min(best_l,r-l+1)

                
                
            last_min[r]=min(last_min[r],best_l)

        return res if res!=1e9 else -1


        