class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=[]
        nums.sort()
        def x(ind,st):
           
            ans.append(st[:])
            for i in range(ind,n):
                if i!=ind and nums[i]==nums[i-1]:
                    continue
                st.append(nums[i])
                
                x(i+1,st)
                st.pop()
            return
        x(0,[])
        return ans