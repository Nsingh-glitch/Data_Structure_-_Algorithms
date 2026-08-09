class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n=len(nums)
        def swap(a,b):
            temp=nums[a]
            nums[a]=nums[b]
            nums[b]=temp

        def Quick_select(l,r):
            
            P=nums[l]
            i=l+1
            j=r
            while i<=j:
                
                if nums[i]<P and nums[j]>P:
                    swap(i,j)
                    i+=1
                    j-=1
                else:

                    if i<=j and nums[i]>=P:
                        i+=1
                    if i<=j and nums[j]<=P:
                        j-=1

            swap(l,j)

            return j
            
        
        def x(l,r):
            ind=Quick_select(l,r)
           
            if ind==k-1:
                return nums[ind]
            elif ind>k-1:
                return x(l,ind-1)
            else:
                return x(ind+1,r)

        return x(0,n-1) 
           