class Solution:
    def largestRectangleArea(self, arr: List[int]) -> int:

        st=[]
        mod=1000000000+7
        n=len(arr)
        prfx=[-1]*n
        suffx=[n]*n


        st=[0]
        for i in range(1,n):
            while st and arr[st[-1]]>=arr[i]:
                st.pop()
            if st :
                prfx[i]=st[-1]

            st.append(i)

        st=[n-1]
        for i in range(n-2,-1,-1):
            while st and arr[st[-1]]>arr[i]:
                st.pop()
            if st :
                suffx[i]=st[-1]

            st.append(i)

      

        ans=0
        for i in range(n):
            p=suffx[i]-prfx[i]-1
          

            ans=max(ans,p*arr[i])
            print(ans,arr[i],prfx[i],suffx[i])

        return ans