class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        st=[]
        n=len(nums)
        nge=[-1]*n

        N=2*n-1
        for  i in range(N,-1,-1):
            ind=i%n
            while st and st[-1]<=nums[ind]:
                st.pop()

            if i<n:
                if st:
                    nge[i]=st[-1]

            st.append(nums[ind])
            
        return nge

        